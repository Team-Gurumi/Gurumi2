import socket
import json
from crypto.aes_util import encrypt

# TCP 클라이언트: 작업 요청 보내기
def send_task_request(target_ip, target_port, task_message):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((target_ip, target_port))

    message_json = json.dumps(task_message)
    encrypted_message = encrypt(message_json)
    client_socket.send(json.dumps(encrypted_message).encode())

    print(f"[요청 전송 완료] {task_message}")

    response = client_socket.recv(1024).decode()
    print(f"[응답 수신] {response}")

    client_socket.close()