import socket
import json
from policy_agent import accept_task
from crypto.aes_util import decrypt

HOST = '0.0.0.0'
PORT = 5000

def start_tcp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"[TCP 서버 대기 중] {HOST}:{PORT}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"[연결 수락] {addr}")

        data = client_socket.recv(4096).decode()
        encrypted_data = json.loads(data)
        decrypted_data = decrypt(encrypted_data)
        request_data = json.loads(decrypted_data)

        if accept_task(request_data):
            response = "요청 수락됨"
        else:
            response = "요청 거절됨"

        client_socket.send(response.encode())
        client_socket.close()

if __name__ == "__main__":
    start_tcp_server()