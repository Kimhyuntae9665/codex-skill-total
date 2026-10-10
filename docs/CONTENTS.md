# 파일 구성과 포함 범위 / File inventory

이 저장소는 Total과 직접 참조하는 일곱 스킬의 **설치 가능한 스냅샷**을 포함합니다. 관련 upstream 프로젝트의 전체 개발 저장소나 사용자 홈을 통째로 복사한 것이 아닙니다.

## 폴더 구조

```text
codex-skill-total/
├── README.md / README.en.md      사용·설치·모델 계약·제한
├── NOTICE.md / LICENSE           자체·third-party 출처/라이선스
├── skills/
│   ├── total/                   SKILL.md, agents/, references/, scripts/
│   ├── council/                 SKILL.md, agents/, assets/, references/
│   ├── ui-ux-pro-max/           SKILL.md, source, agents/, data/, scripts/
│   ├── graphify/                SKILL.md, source, agents/, references/, notices
│   ├── impeccable/              SKILL.md, source, agents/, reference/, scripts/
│   ├── archify/                 CLI, renderers, schemas, assets, examples, references
│   ├── karpathy-guidelines/     SKILL.md, SOURCE.md, upstream snapshot
│   └── 6-1-sol-orch/            SKILL.md, agents/, LICENSE, NOTICE
├── manifests/
│   ├── source-coverage.json      원본 모든 파일의 포함/제외 및 원본·공개 SHA-256
│   └── bundle.sha256.json        최종 저장소 파일별 SHA-256
├── scripts/                     번들 검증, 설치·백업
├── tests/                       신규 설치·충돌·백업·해시 위변조 검사
└── .github/workflows/           Windows/Linux 검증 CI
```

## 수집과 공개본 파일 수

원본 파일 수는 설치본 기준이며, 공개본에는 이식용 지침과 누락된 upstream 고지/라이선스가 추가됩니다. 제외된 원본 파일은 생성된 Python bytecode/cache뿐입니다.

| 스킬 | 포함한 원본 파일 | 제외한 캐시 | 공개본 파일 | 공개본 바이트 |
|---|---:|---:|---:|---:|
| `6-1-sol-orch` | 4 | 0 | 4 | 16,840 |
| `archify` | 317 | 0 | 317 | 10,648,793 |
| `council` | 7 | 0 | 8 | 32,306 |
| `graphify` | 13 | 0 | 15 | 99,814 |
| `impeccable` | 65 | 0 | 66 | 21,461,721 |
| `karpathy-guidelines` | 3 | 0 | 4 | 8,001 |
| `total` | 5 | 1 | 7 | 23,110 |
| `ui-ux-pro-max` | 71 | 6 | 71 | 3,625,937 |

모든 원본 경로는 `source-coverage.json`에 상대경로로 기록되어 있습니다. 설치본의 SKILL.md를 이식 수정한 경우 원본 hash와 공개본 hash를 따로 유지합니다. 원래 upstream SKILL.source.md는 그대로 포함했습니다.

## 중요한 하위 파일

- **Total:** `references/council-routing.md`는 고정 패킷/적용 지도, `application-and-validation.md`는 결과별 검증, `portfolio-guidance.md`는 개인 파일에 의존하지 않는 제작/사실 기준입니다. `scripts/check_dependencies.py`는 번들 형제 스킬을 우선 조회합니다.
- **Council:** `assets/council-sol.toml`, `council-astra.toml`, `council-luna.toml`과 `references/council-recipes.md`, `council-evaluation.md`를 포함합니다. 프로필 자산은 글로벌 설정에 자동 등록하지 않습니다.
- **UI/UX Pro Max:** `scripts/search.py`와 내부 검색 모듈, `data/`의 스타일·제품·UX·차트·폰트·아이콘 및 스택 데이터가 함께 들어 있습니다. 카탈로그는 모든 폰트 바이너리의 배포본이 아닙니다.
- **Graphify:** 설치본의 전체 references와 SKILL.source.md를 포함합니다. 별도 실행 패키지는 `graphifyy[pdf,office,mcp]==0.9.84`; Python 가상환경을 GitHub에 올리지 않습니다.
- **Impeccable:** `reference/`의 모든 설치된 playbook, `scripts/impeccable`, `impeccable.cmd`, `VERSION`, `scripts/data/`, browser 보조 스크립트, `scripts/bin/windows-x64/impeccable.exe`를 포함합니다. 다른 플랫폼의 native engine은 launcher의 별도 다운로드 경로입니다.
- **Archify:** `bin/`, `renderers/`, `schemas/`, `assets/`, `examples/`, `references/`와 설치본에 있던 검사·생성 자원을 그대로 보존합니다. `package.json`의 upstream 개발 scripts 일부는 부모 저장소 파일을 사용하므로 전체 개발 테스트가 필요하면 원본 upstream 저장소를 받으세요. 일반 CLI runtime은 이 번들에서 검증합니다.

## 포함하지 않는 것

인증 토큰·쿠키·SSH 키·계정 설정·개인 채용 원장·private guidance·과거 대화 기록·글로벌 Python/Node 환경·무관한 다른 스킬은 포함하지 않습니다. Windows native engine 이외의 실행 환경은 README의 명시적 설치 방법으로 준비합니다. 이는 의도적 범위이며 숨긴 파일 누락이 아닙니다.

## 검증 방법

`python scripts/validate_bundle.py`는 최종 파일 집합과 SHA-256, 스킬 진입점, runtime Markdown 상대 링크, 민감 경로/credential 형태, source coverage hash를 검사합니다. `python -m unittest discover -s tests -v`는 설치의 원본 바이트 보존·충돌 전 중단·백업 교체·변조 거부를 검증합니다. CI도 같은 명령을 Windows/Linux에서 실행합니다.

이 검사는 패키지/설치 검증이며, 실제 Council 모델 접근·모든 OS native engine·사용자 프로젝트의 품질 향상·Codex UI 자동 검색을 입증하지 않습니다.
