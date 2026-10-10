"""Install all bundled skills; verify bytes first, abort conflicts, back up opt-in overwrite."""
import argparse
from datetime import datetime,timezone
import json
import os
from pathlib import Path
import shutil
import sys

sys.dont_write_bytecode=True
from validate_bundle import SKILLS,verify


def install(dest,dry_run=False,overwrite=False):
    repo=Path(__file__).resolve().parents[1]
    verify(repo)
    dest=Path(dest).expanduser().resolve()
    targets=[dest/name for name in SKILLS]
    conflicts=[p for p in targets if p.exists()]
    if conflicts and not overwrite:
        raise ValueError('Existing skill directories; no files changed. Choose another --dest or use --overwrite with backups: '+', '.join(p.name for p in conflicts))
    if any(p.resolve().parent!=dest or p.is_symlink() for p in targets):
        raise ValueError('Unsafe target or symlink; no files changed.')
    result={'destination':str(dest),'skills':list(SKILLS),'dry_run':dry_run,'backup':None}
    if dry_run: return result
    stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    backup=dest/'.total-backups'/stamp
    failed=dest/'.total-failed'/stamp
    if not backup.resolve().is_relative_to(dest) or not failed.resolve().is_relative_to(dest):
        raise ValueError('Backup/recovery directory escapes the chosen destination; no files changed.')
    completed=[]
    backed_up=[]
    dest.mkdir(parents=True,exist_ok=True)
    try:
        for target in targets:
            if target.exists():
                backup.mkdir(parents=True,exist_ok=True)
                target.rename(backup/target.name)
                backed_up.append(target)
            completed.append(target)
            shutil.copytree(repo/'skills'/target.name,target)
        if os.name!='nt':
            launcher=dest/'impeccable/scripts/impeccable'
            launcher.chmod(launcher.stat().st_mode|0o111)
    except Exception:
        # Preserve partial outputs separately rather than deleting user files.
        for target in reversed(completed):
            if target.exists():
                failed.mkdir(parents=True,exist_ok=True)
                target.rename(failed/target.name)
            if target in backed_up: (backup/target.name).rename(target)
        raise
    result['backup']=str(backup) if backed_up else None
    return result


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dest',type=Path,default=Path(os.environ.get('CODEX_HOME',str(Path.home()/'.codex')))/'skills')
    parser.add_argument('--dry-run',action='store_true')
    parser.add_argument('--overwrite',action='store_true',help='Back up conflicting target directories before replacement.')
    args=parser.parse_args()
    try: print(json.dumps(install(args.dest,args.dry_run,args.overwrite),ensure_ascii=False,indent=2))
    except (ValueError,OSError) as error:
        print(str(error),file=sys.stderr)
        raise SystemExit(2)
