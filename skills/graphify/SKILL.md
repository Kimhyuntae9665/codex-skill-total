---
name: graphify
description: Build, update, and query knowledge graphs from code and documents. Use for repository architecture, dependencies, source-backed paths, change impact, or questions against an existing graphify-out graph.
metadata:
  version: "0.9.84"
  adapter: "Portable Codex"
---

# Graphify

The bundled files contain the official skill workflow and references; the Python CLI is a separately installed pinned dependency. Install `graphifyy[pdf,office,mcp]==0.9.84` with uv and Python 3.11 as documented in the repository README. Do not register hooks, watch, or MCP by default.

Keep extracted, inferred and ambiguous relations distinct and cite current source files. A graph's prediction is not a test result. Resolve a PATH command with `Get-Command graphify` / `command -v graphify`; the usual uv tool path on Windows is `$HOME/.local/bin/graphify.exe`, and UV_TOOL_BIN_DIR can override it.

For an existing `graphify-out/graph.json`, query first unless the user requests rebuilding. Check whether it matches current sources.

```powershell
$graphify = Join-Path $env:USERPROFILE '.local/bin/graphify.exe'
& $graphify query 'What calls the request handler?' --budget 1500
& $graphify path 'Handler' 'Repository'
& $graphify explain 'Handler'
```

For a new local code-only AST graph (no model or API key required), keep cwd at the target project or an authorized analysis copy:

```powershell
& $graphify extract '.' --code-only
& $graphify cluster-only '.' --no-label
```

Extraction creates analysis files. Preserve source and prior graphs; do not force a partial replacement when extraction is incomplete. Check command exits, artifacts, input coverage and unsupported languages.

For documents/media, mixed corpora, semantic extraction, advanced exports, updates, watch or MCP, read [the preserved official workflow](SKILL.source.md) and its relevant references. Translate POSIX examples for the active shell. PDF/Office parsing extras are installed by the pinned command, but semantic interpretation still needs an available, authorized backend. Do not assume credentials, external uploads or database mutations are authorized.
