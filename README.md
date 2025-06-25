✔️ node/: 한 폴더에서 수요 + 공급 모두 담당  
✔️ core/: 작업 처리 핵심 (작업 관리, Kata 실행, 모니터링, 리포트 관리)  
✔️ network/: TCP 서버/클라이언트 → 공용 사용  
✔️ crypto/: 암호화 전용 유틸 (공용 사용)  
✔️ service.py: 하나의 Python 스크립트에서 "내가 지금 수요 모드인지, 공급 모드인지" 스위칭 제어  
  
```
mutual_cloud/
├── node/                    # 단일 노드 (P2P 역할 수행)
│   ├── core/
│   │   ├── task_manager.py      # 작업 요청/수신/처리 통합
│   │   ├── container_executor.py# Kata 작업 실행
│   │   ├── resource_monitor.py  # 자원 모니터링
│   │   └── report_manager.py    # 리포트 생성/전송
│   ├── network/
│   │   ├── tcp_server.py        # TCP 서버 (작업 수신)
│   │   └── tcp_client.py        # TCP 클라이언트 (작업 송신)
│   ├── crypto/
│   │   ├── aes_util.py          # AES 암호화/복호화
│   │   └── key_manager.py       # 키 관리 (필요 시)
│   ├── service.py               # 전체 흐름 제어 (수요/공급 스위칭)
│   ├── launcher.py              # 실행 진입점
│   └── config.py                # Tailscale IP, 포트, 암호화 키
│
├── central/                  # 중앙 서버 (리포트 수신)
│   ├── report_receiver.py       # 리포트 수신
│   ├── report_db.py             # DB 저장
│   └── report_verifier.py       # 무결성 검증
│
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
