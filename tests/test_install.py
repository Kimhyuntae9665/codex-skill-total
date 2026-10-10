import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.dont_write_bytecode=True
sys.path.insert(0,str(ROOT/'scripts'))
from install import install
from validate_bundle import SKILLS,verify


class BundleInstallation(unittest.TestCase):
    def test_dry_run_is_read_only(self):
        with tempfile.TemporaryDirectory() as folder:
            target=Path(folder)/'skills'
            result=install(target,dry_run=True)
            self.assertTrue(result['dry_run'])
            self.assertFalse(target.exists())

    def test_fresh_conflict_and_backup(self):
        with tempfile.TemporaryDirectory() as folder:
            target=Path(folder)/'skills'
            install(target)
            hashes=json.loads((ROOT/'manifests/bundle.sha256.json').read_text())['files']
            for path,digest in hashes.items():
                if path.startswith('skills/'):
                    installed=target/Path(path).relative_to('skills')
                    self.assertEqual(hashlib.sha256(installed.read_bytes()).hexdigest(),digest,path)
            marker=target/'total/user-note.txt'
            marker.write_text('preserve me',encoding='utf-8')
            with self.assertRaises(ValueError): install(target)
            self.assertEqual(marker.read_text(),'preserve me')
            replacement=install(target,overwrite=True)
            backup=Path(replacement['backup'])
            self.assertEqual((backup/'total/user-note.txt').read_text(),'preserve me')
            self.assertFalse(marker.exists())
            self.assertTrue(all((target/name/'SKILL.md').is_file() for name in SKILLS))
            self.assertEqual(verify(ROOT)['status'],'pass')

    def test_collision_aborts_before_partial_install(self):
        with tempfile.TemporaryDirectory() as folder:
            target=Path(folder)/'skills'
            (target/'archify').mkdir(parents=True)
            (target/'archify/keep.txt').write_text('original')
            with self.assertRaises(ValueError): install(target)
            self.assertEqual({p.name for p in target.iterdir()},{'archify'})
            self.assertEqual((target/'archify/keep.txt').read_text(),'original')

    def test_installer_rejects_changed_checksum_before_writes(self):
        with tempfile.TemporaryDirectory() as folder:
            fake=Path(folder)/'copy'
            (fake/'manifests').mkdir(parents=True)
            (fake/'x.txt').write_text('tampered')
            (fake/'manifests/bundle.sha256.json').write_text(json.dumps({'files':{'x.txt':hashlib.sha256(b'original').hexdigest()}}))
            with self.assertRaisesRegex(ValueError,'Checksum mismatch'): verify(fake)


if __name__=='__main__': unittest.main()
