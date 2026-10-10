# Total — Council-first Codex skill bundle

Use **`$total`** with a project or portfolio to discover improvements, apply the relevant changes and verify the outcome. Council reviews the target first; UI/UX Pro Max, Graphify, Impeccable and Archify provide the design, source analysis, interface refinement and interactive explanation capabilities.

[한국어](README.md) · [File inventory](docs/CONTENTS.md) · [Installer](scripts/install.py) · [Attribution](NOTICE.md)

**Target and evidence → five independent Council reviews → Sol synthesis and parent fidelity check → applicability of all four tools → scoped improvements → execution and before/after verification.** Tools run where they help, with documented reasons for unused routes; their execution order follows dependencies.

## Complete skill payload

The `skills/` directory contains eight sibling skill trees:

| Skill | Responsibility and bundled resources |
|---|---|
| [total](skills/total/SKILL.md) | Integration, Council routing, application/validation and portable portfolio guidance, dependency checker |
| [council](skills/council/SKILL.md) | Independent review contract, three reusable agent profile TOMLs, recipes and evaluation guidance |
| [ui-ux-pro-max](skills/ui-ux-pro-max/SKILL.md) | UI/design systems, search scripts, style/UX/font/icon/stack data |
| [graphify](skills/graphify/SKILL.md) | Source-backed structure, calls and impact; official workflow and extraction/query/update references |
| [impeccable](skills/impeccable/SKILL.md) | Interface quality and usability, all installed playbooks/scripts/data, Windows x64 native engine |
| [archify](skills/archify/SKILL.md) | Interactive diagrams, CLI/renderers/viewer/schemas/templates/examples/validation resources |
| [karpathy-guidelines](skills/karpathy-guidelines/SKILL.md) | Scope, assumptions, focused changes and verification; source attribution and upstream snapshot |
| [6-1-sol-orch](skills/6-1-sol-orch/SKILL.md) | Optional authorized implementation delegation with role/file ownership boundaries |

The last two are supporting dependencies of Total. They do not run a second Council for the same decision. Runtime references remain inside the bundle; original upstream entrypoints are retained as `SKILL.source.md` where available. Private career records and the original author's PC guidance/configuration are excluded.

## Install

Requirements: a Codex host supporting skills, Python 3.11 recommended, Node.js **18+**, and [uv](https://docs.astral.sh/uv/getting-started/installation/) for the Graphify CLI. Council requires the models/reasoning and subagent capabilities listed below. Copying files does not grant model access or additional slots.

```sh
git clone https://github.com/Kimhyuntae9665/codex-skill-total.git
cd codex-skill-total
python3 scripts/install.py --dry-run
python3 scripts/install.py
uv tool install --python 3.11 'graphifyy[pdf,office,mcp]==0.9.84'
```

On Windows use `python` instead of `python3`. If only uv is available, use `uv run --python 3.11 python scripts/install.py`. Node.js and uv are not installed automatically. Skills should be available on the next Codex turn.

The default destination is `$CODEX_HOME/skills` or `~/.codex/skills`. Existing target directories cause an abort **before any changes**. Use an isolated destination to test, or opt into backup replacement:

```sh
python3 scripts/install.py --dest ./test-skills --dry-run
python3 scripts/install.py --dest ./test-skills
python3 scripts/install.py --overwrite
```

Overwrite preserves existing targets under `.total-backups/<UTC timestamp>/`. A project-local destination such as `./.codex/skills` is also supported. Commands must resolve against the actual installation directory when using a custom destination. Total's checker prefers bundled siblings; check your host's skill search paths if duplicate skill names already exist elsewhere. Global `config.toml` is never modified.

## Use

```text
$total review this project's structure, UI and usability, then apply and verify improvements.
$total C:/path/to/project — preserve existing behavior and user changes.
$total improve the attached portfolio while preserving factual experience and page constraints.
$total review only; do not modify the project.
```

Default requests apply and verify scoped changes. Review-only requests return findings without changing source artifacts. A clear target needs no repeated approval; an absent or conflicting target needs resolution. Publication, deployment, messaging and final submissions follow the user's separate applicable authorization.

## Council contract

| Role | Model | Reasoning |
|---|---|---|
| Strategist | `gpt-6.1-sol` | `max` |
| Skeptic | `gpt-6-astra` | `max` |
| Creative | `gpt-6-astra` | `max` |
| Operator | `gpt-6.1-sol` | `max` |
| Audience Advocate | `gpt-6-luna` | `max` |
| Synthesizer | `gpt-6.1-sol` | `max` |

Five fresh independent roles receive the same frozen packet. Five valid terminal briefs must pass the gate before Sol synthesis and the parent's fidelity check permit implementation. One failed-role retry is allowed. Missing required models/reasoning do not silently reduce this contract or produce a Full Council label. Process completion, evidence confidence and unresolved claims are reported separately, including Creative's actual proposal/disposition.

The reusable TOMLs in [Council assets](skills/council/assets) can be used where the host supports them. If named profiles are unavailable but exact model/reasoning selection exists, use Council's explicit-model path. Invocation does not switch the active root model. Fast service is requested only when the API explicitly supports it; otherwise record exposed defaults and unknowns.

## Included files versus external runtimes

- Graphify's **CLI/environment is external**, installed by the pinned uv command. Local code-only AST extraction requires no API key; semantic document/media extraction needs an available authorized backend. MCP library installation does not register a Codex connector. Hooks/watch are not enabled.
- Impeccable's **Windows x64 0.1.14 binary is included**. Other native binaries are not; upstream launchers can download and hash-verify the pinned engine on first use. All installed references/scripts/data are included.
- Archify's ordinary CLI works from its bundled resources with Node.js. Upstream full-repository development generators and `npm test` are not the validation path for this skill snapshot.
- UI/UX Pro Max includes catalogs/scripts, not all font binaries. Catalog fallbacks must be checked against the actual surface.

Graph relations, static detection, automated browser receipts, manual visual review and functional tests are distinct evidence. Impeccable keeps its bounded inspect/fix/confirm pass. An early Archify flow diagram is a conditional option: test one preserved flow to see whether it identifies missing guidance/edit locations and whether changed screen states match actual behavior. Render final portfolios and inspect factual claims, job-task connections, screenshot boundaries and simulation callouts. Do not invent metrics or convert demos into production evidence.

## Integrity and validation

```sh
python3 scripts/validate_bundle.py
python3 -m unittest discover -s tests -v
```

[Source coverage](manifests/source-coverage.json) accounts for every file in the eight selected installed skill trees, with original/published hashes and adaptations. Only generated Python caches are excluded. The [final checksum manifest](manifests/bundle.sha256.json) checks the repository inventory, hashes, local runtime Markdown references, entrypoints and private-path/credential-shaped content. Windows/Linux CI checks bundle integrity, fresh installation, collision abort and backup replacement.

These checks demonstrate packaging and installer behavior. They do not prove project-quality gains, all native platform behavior, implicit host discovery, model availability or cost. See [NOTICE.md](NOTICE.md) for mixed licensing, upstream versions and separate reviewed-commit versus registry-payload identifiers. Total/Council/package documentation is MIT; bundled third-party files retain their original licenses and mark terms.
