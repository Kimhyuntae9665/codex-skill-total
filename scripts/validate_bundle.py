"""Validate exact bundle inventory, entrypoints, relative references and privacy."""
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote

SKILLS=('total','council','ui-ux-pro-max','graphify','impeccable','archify','karpathy-guidelines','6-1-sol-orch')


def verify(root):
    root=Path(root).resolve()
    manifest=json.loads((root/'manifests/bundle.sha256.json').read_text(encoding='utf-8'))
    expected=manifest['files']
    actual={p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file()
            and '.git' not in p.relative_to(root).parts and '__pycache__' not in p.parts
            and p.relative_to(root).as_posix()!='manifests/bundle.sha256.json'}
    if set(expected)!=actual:
        raise ValueError('Inventory mismatch: missing='+str(sorted(set(expected)-actual))+' extra='+str(sorted(actual-set(expected))))
    for rel,digest in expected.items():
        path=(root/rel).resolve()
        if not path.is_relative_to(root) or hashlib.sha256(path.read_bytes()).hexdigest()!=digest:
            raise ValueError('Checksum mismatch or unsafe path: '+rel)
    checked_links=0
    for name in SKILLS:
        entry=root/'skills'/name/'SKILL.md'
        text=entry.read_text(encoding='utf-8-sig')
        header=re.match(r'\A---\s*\n(.*?)\n---(?:\s|$)',text,re.S)
        if not header or not re.search(r'^name:\s*[\"\']?'+re.escape(name)+r'[\"\']?\s*$',header.group(1),re.M):
            raise ValueError('Invalid skill entrypoint: '+name)
        if not re.search(r'^description:\s*\S',header.group(1),re.M):
            raise ValueError('Missing skill description: '+name)
        # Follow runtime Markdown references, not upstream development scripts or illustrative code snippets.
        for doc in (entry,*sorted((entry.parent/'references').glob('*.md')),*sorted((entry.parent/'reference').glob('*.md'))):
            if not doc.exists(): continue
            content=doc.read_text(encoding='utf-8-sig')
            # Fenced command/example payloads can contain illustrative links.
            prose=re.sub(r'```.*?```','',content,flags=re.S)
            for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)',prose):
                target=target.split('#',1)[0]
                if not target or re.match(r'^[a-zA-Z][\w+.-]*:',target): continue
                target=unquote(target)
                if any(c in target for c in '<>{}'): continue
                path=(doc.parent/target).resolve()
                if not path.is_relative_to(root) or not path.exists():
                    raise ValueError('Missing local reference: '+doc.relative_to(root).as_posix()+' -> '+target)
                checked_links+=1
    privacy_patterns=[r'C:[\\/]+Users[\\/]+user[\\/]',r'-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----',r'\bgh[pousr]_[A-Za-z0-9]{30,}',r'\bgithub_pat_[A-Za-z0-9_]{30,}']
    for rel in expected:
        path=root/rel
        if path.suffix in {'.exe','.png','.jpg','.webp'}: continue
        try: content=path.read_text(encoding='utf-8-sig')
        except UnicodeError: continue
        if any(re.search(pattern,content) for pattern in privacy_patterns):
            raise ValueError('Private path/credential-shaped content detected in '+rel+'; contents suppressed')
    coverage=json.loads((root/'manifests/source-coverage.json').read_text(encoding='utf-8'))
    for record in coverage['included_source_files']:
        if expected.get(record['published_path'])!=record['published_sha256']:
            raise ValueError('Source coverage digest not synchronized: '+record['published_path'])
    for doc in [root/'README.md',root/'README.en.md',root/'NOTICE.md',*sorted((root/'docs').glob('*.md'))]:
        for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)',doc.read_text(encoding='utf-8')):
            target=target.split('#',1)[0]
            if not target or re.match(r'^[a-zA-Z][\w+.-]*:',target): continue
            path=(doc.parent/unquote(target)).resolve()
            if not path.is_relative_to(root) or not path.exists():
                raise ValueError('Missing repository documentation link: '+doc.name+' -> '+target)
            checked_links+=1
    return {'status':'pass','bundle_files':len(expected),'skills':list(SKILLS),'runtime_markdown_links':checked_links,
            'covered_source_files':len(coverage['included_source_files']),'intentional_exclusions':len(coverage['excluded_source_files'])}


if __name__=='__main__':
    print(json.dumps(verify(Path(__file__).resolve().parents[1]),ensure_ascii=False,indent=2))
