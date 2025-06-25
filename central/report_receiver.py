# mutual_cloud/central/report_receiver.py
import socket
import json
from report_db import save_report_to_csv

HOST = '0.0.0.0'
PORT = 6000

# 리포트 수신 서버
def start_report_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"[리포트 서버 실행 중] {HOST}:{PORT}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"[연결 수락] {addr}")

        data = client_socket.recv(4096).decode()
        report = json.loads(data)
        print(f"[리포트 수신] {report}")

        save_report_to_csv(report)
        print(f"[리포트 저장 완료]")

        client_socket.close()

if __name__ == "__main__":
    start_report_server()