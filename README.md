✔️ node/: 한 폴더에서 수요 + 공급 모두 담당  
✔️ core/: 작업 처리 핵심 (작업 관리, Kata 실행, 모니터링, 리포트 관리)  
✔️ network/: TCP 서버/클라이언트 → 공용 사용  
✔️ crypto/: 암호화 전용 유틸 (공용 사용)  
✔️ service.py: 하나의 Python 스크립트에서 "내가 지금 수요 모드인지, 공급 모드인지" 스위칭 제어
✔️ policy_agent.py: 자원 사용률 기반으로 요청 수락/거절 판단 (분산 자율 정책 구현의 핵심)  
✔️ http_server.py: 파일 수신 및 결과 반환을 HTTP로 처리 (REST API 기반 전송)  
✔️ container_executor.py: 작업을 Docker 또는 Kata Containers 격리 환경에서 실행  
✔️ report_manager.py: 작업 결과를 리포트로 정리하여 중앙에 전송 (수요자 피드백 포함 가능)  
✔️ central/: 리포트 보관소 역할 (완전한 중앙 제어자가 아님, 장애 감시/기록용)  
✔️ tests/: 각 모듈 기능이 올바르게 작동하는지 자동화된 단위 테스트 수행  
✔️ utils/: 압축, 파일 I/O 등 반복되는 기능을 정리한 보조 함수 공간  
✔️ requirements.txt: 실행에 필요한 필수 라이브러리 정의 (Flask, requests 등)  
✔️ dev-requirements.txt: 개발자용 테스트/디버깅 도구 정의 (pytest, docker 등)

  
```
mutual_cloud/
├── node/                            # P2P 단일 노드 (수요/공급 역할 모두 수행)
│   ├── core/                        # 핵심 기능 모듈
│   │   ├── task_manager.py          # 작업 수신/분배/관리 통합 컨트롤러
│   │   ├── container_executor.py    # Kata Containers 또는 Docker 기반 작업 실행
│   │   ├── resource_monitor.py      # 자원 사용률(CPU, 메모리 등) 실시간 모니터링
│   │   └── report_manager.py        # 실행 결과 리포트 생성 및 송신
│
│   ├── network/                     # 통신 계층 모듈 (P2P 직접 연결)
│   │   ├── tcp_server.py            # TCP 서버 - 수요자 요청 수신 처리
│   │   ├── tcp_client.py            # TCP 클라이언트 - 공급자에 작업 전송
│   │   └── http_server.py           # (추가) Flask 기반 REST API 서버 (작업 수신/결과 반환)
│
│   ├── crypto/                      # 보안 처리 모듈
│   │   ├── aes_util.py              # AES 대칭키 암호화/복호화 함수
│   │   └── key_manager.py           # 키 생성 및 관리 기능 (옵션)
│
│   ├── policy_agent.py              # (추가) 요청 수락/거절을 판단하는 자율 정책 기반 로직
│   ├── service.py                   # 전체 실행 흐름 제어 (수요/공급 역할 전환 등)
│   ├── launcher.py                  # 실행 진입점 (main 함수)
│   └── config.py                    # 시스템 설정 (VPN IP, 포트, 키, 경로 등)
│
├── central/                         # 중앙 서버 기능 (중간 기록/로그용 보조 서버)
│   ├── report_receiver.py           # 리포트 수신 (노드 → 중앙)
│   ├── report_db.py                 # 리포트 DB 저장 (MySQL/SQLite)
│   └── report_verifier.py           # 리포트 무결성 검증 (해시/서명 기반)
│
├── utils/                           # (추가) 보조 유틸리티 함수 모음
│   └── file_helper.py               # 파일 입출력, 압축/해제 등 일반 처리 유틸
│
├──tests/
|  ├── test_core.py       # core 모듈의 핵심 기능을 테스트 (작업 실행, 결과 생성 등)
|  ├── test_network.py    # 네트워크 모듈 테스트 (작업 수신/전송, HTTP 응답 등)
|  └── test_crypto.py     # 암호화 모듈 테스트 (AES 암복호화 정상 동작 여부)
│
├── requirements.txt                 # Python 패키지 의존성 목록
├── dev-requirments.txt              # 개발/테스트용 패키지 의존성 목록
└── README.md                       
```


지금 작성된 버전은 기본 구조 + 데이터 흐름 완성 버전이고, 이후에 작업 요청 JSON 고도화, Kata Container 연동 등 세부 단계로 확장  

🔗 전체 작성 파일
central/report_db.py : 리포트 CSV 저장

central/report_receiver.py : 리포트 TCP 수신 서버

central/report_verifier.py : 리포트 무결성 검증 (hash 기반)

node/config.py : IP, 포트 설정

node/launcher.py : 서비스 실행 진입점

node/service.py : 더미 작업 수행 + 리포트 전송
