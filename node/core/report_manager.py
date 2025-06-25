# node/core/report_manager.py

import hashlib
import socket
import json

def create_and_send_report(result):
    report = {
        "result": result,
        "task_id": generate_task_id(result),
    }

    report['hash'] = generate_hash(report)

    send_report_to_central(report)

def generate_task_id(result):
    return hashlib.sha256(result.encode()).hexdigest()[:8]

def generate_hash(report):
    raw = json.dumps(report, sort_keys=True).encode()
    return hashlib.sha256(raw).hexdigest()

def send_report_to_central(report):
    central_ip = "central_server_ip"  # 수정 필요
    central_port = 5000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((central_ip, central_port))
        s.sendall(json.dumps(report).encode())

    print("[ReportManager] 리포트 중앙 서버 전송 완료")
