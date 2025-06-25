# node/core/task_manager.py

from node.network.tcp_server import start_server
from node.network.tcp_client import send_task
from node.crypto.aes_util import encrypt_data, decrypt_data
from node.core.container_executor import execute_in_container
from node.core.report_manager import create_and_send_report
from node.policy_agent import is_request_accepted

class TaskManager:
    def __init__(self, mode, my_ip, my_port):
        self.mode = mode  # 'client' or 'server'
        self.my_ip = my_ip
        self.my_port = my_port

    def start_server_mode(self):
        # 서버 모드: 작업 수신
        print("[TaskManager] 서버 모드 실행 중...")
        start_server(self.handle_received_task, self.my_ip, self.my_port)

    def start_client_mode(self, target_ip, target_port, task_data):
        # 클라이언트 모드: 작업 전송
        print(f"[TaskManager] {target_ip}로 작업 전송 시도 중...")
        encrypted_task = encrypt_data(task_data)
        send_task(target_ip, target_port, encrypted_task)

    def handle_received_task(self, encrypted_task, sender_ip):
        print(f"[TaskManager] {sender_ip}로부터 작업 수신")

        if not is_request_accepted(sender_ip):
            print("[TaskManager] 작업 요청 거절됨")
            return

        task_data = decrypt_data(encrypted_task)
        print("[TaskManager] 작업 복호화 완료. 작업 실행 중...")

        result = execute_in_container(task_data)
        create_and_send_report(result)

        print("[TaskManager] 작업 완료 및 리포트 전송 완료.")
