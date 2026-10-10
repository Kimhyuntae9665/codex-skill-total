"""Read-only Total dependency inventory; existence is not runtime validation."""
import argparse
import json
import os
from pathlib import Path
import re
import shutil


def inventory(home):
    codex_home = Path(os.environ.get("CODEX_HOME", str(home / ".codex"))) if home == Path.home() else home / ".codex"
    roots = [codex_home / "skills", home / ".agents" / "skills", home / ".codex" / "skills"]
    if home == Path.home():
        roots.insert(0, Path(__file__).resolve().parents[2])
    expected = {
        "council": [],
        "ui-ux-pro-max": ["scripts/search.py", "data"],
        "graphify": [],
        "impeccable": ["scripts/impeccable.cmd"] if os.name == "nt" else ["scripts/impeccable"],
        "archify": ["bin/archify.mjs", "schemas", "assets"],
        "karpathy-guidelines": [],
        "6-1-sol-orch": [],
    }
    rows = []
    for name, resources in expected.items():
        path = next((root / name / "SKILL.md" for root in roots if (root / name / "SKILL.md").is_file()), None)
        issues = []
        if path is None:
            issues.append("missing_entrypoint")
        else:
            source = path.read_text(encoding="utf-8-sig")
            frontmatter = re.match(r"\A---\s*\n(.*?)\n---(?:\s|$)", source, re.S)
            names = re.findall(r"^name:\s*([^\n]+)$", frontmatter.group(1), re.M) if frontmatter else []
            if len(names) != 1 or names[0].strip().strip("\"'") != name:
                issues.append("invalid_skill_name_or_frontmatter")
            issues.extend("missing_resource:" + r for r in resources if not (path.parent / r).exists())
        rows.append({"name": name, "path": str(path) if path else None, "available": not issues, "issues": issues})
    graph_exe = home / ".local" / "bin" / ("graphify.exe" if os.name == "nt" else "graphify")
    return {
        "skills": rows,
        "runtime_candidates": {"node": shutil.which("node"), "python": shutil.which("python"),
                               "graphify": str(graph_exe) if graph_exe.is_file() else shutil.which("graphify")},
        "all_skill_files_available": all(row["available"] for row in rows),
        "limits": "File checks only; models, engine execution, semantic backends and visual quality are not tested.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--home", type=Path, default=Path.home(), help="Home directory; override for isolated fixtures.")
    args = parser.parse_args()
    result = inventory(args.home.resolve())
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result["all_skill_files_available"] else 2)
