# mutual_cloud/node/service.py
import socket
import json
import time
import random
from config import REPORT_SERVER_IP, REPORT_SERVER_PORT

# 더미 작업 수행 + 자원 사용량 측정
def perform_dummy_task():
    print("[작업 시작]")
    time.sleep(random.uniform(1, 3))  # 작업 수행 시간 시뮬레이션
    result = random.randint(100, 999)  # 작업 결과 시뮬레이션
    cpu_usage = random.uniform(10.0, 50.0)
    ram_usage = random.uniform(100.0, 500.0)
    disk_io = random.uniform(50.0, 200.0)
    network_io = random.uniform(1.0, 10.0)
    print("[작업 완료]")

    return {
        'task_id': f'task_{random.randint(1000, 9999)}',
        'cpu_usage': cpu_usage,
        'ram_usage': ram_usage,
        'disk_io': disk_io,
        'network_io': network_io,
        'result': result
    }

# 리포트 전송
def send_report(report_data):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((REPORT_SERVER_IP, REPORT_SERVER_PORT))

    report_json = json.dumps(report_data)
    client_socket.send(report_json.encode())
    print("[리포트 전송 완료]")

    client_socket.close()

# 전체 흐름 실행
def start_service():
    task_result = perform_dummy_task()
    send_report(task_result)
    print("[서비스 종료]")
