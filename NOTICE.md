# Attribution and license scope

Total's integration instructions, Council snapshot, packaging scripts and repository documentation are user-authored work distributed under the root MIT license. Bundled third-party skills retain their own licenses; the root license does not relicense those files or brand marks.

| Component | Origin | License / retained notice |
|---|---|---|
| UI/UX Pro Max | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | [MIT](skills/ui-ux-pro-max/LICENSE), copyright Next Level Builder |
| Graphify | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | [Apache-2.0](skills/graphify/LICENSE), [NOTICE](skills/graphify/NOTICE), [retained MIT text](skills/graphify/LICENSE-MIT) |
| Impeccable | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | [Apache-2.0](skills/impeccable/LICENSE), [third-party notice](skills/impeccable/NOTICE.md); Windows engine is the upstream distributed binary |
| Archify | [tt-a1i/archify](https://github.com/tt-a1i/archify) | [MIT](skills/archify/LICENSE), [third-party marks and terms](skills/archify/THIRD_PARTY_NOTICES.md) |
| Karpathy Guidelines | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | Upstream skill declares MIT; [source attribution and unmodified snapshot](skills/karpathy-guidelines/SOURCE.md) retained |
| 6.1 Sol Orch | [Kimhyuntae9665/codex-skill-6-1-sol-orch](https://github.com/Kimhyuntae9665/codex-skill-6-1-sol-orch), derived from donvito/codex-astra-luna-orchestrator | [Apache-2.0](skills/6-1-sol-orch/LICENSE), [NOTICE](skills/6-1-sol-orch/NOTICE) |

Public adaptations replace one-PC paths with installation-relative paths, add portable target/portfolio guidance, and keep original upstream entrypoints as SKILL.source.md where they were already installed. Source and published hashes plus upstream versions/commits are recorded in [source-coverage.json](manifests/source-coverage.json). Reviewed GitHub commits for registry packages are source-review identifiers, not proof that the npm/PyPI payload is byte-identical to that commit.

Archify preserves source/license/guideline metadata for embedded marks. Its own MIT license does not replace the individual mark terms. UI/UX Pro Max contains font and icon catalogs and their metadata, not a blanket license to download or redistribute every listed font. Impeccable's platform guidance attribution is retained in its third-party notice. The underlying tools remain projects of their respective authors; this bundle does not imply their endorsement.
