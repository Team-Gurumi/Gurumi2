# mutual_cloud/central/report_db.py
import csv
from datetime import datetime

# 리포트를 CSV로 저장
def save_report_to_csv(report_data, file_path='report_data.csv'):
    fieldnames = ['timestamp', 'task_id', 'cpu_usage', 'ram_usage', 'disk_io', 'network_io', 'result']

    # 파일이 없으면 헤더 생성
    try:
        with open(file_path, 'x', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
    except FileExistsError:
        pass

    # 리포트 저장
    with open(file_path, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        report_data['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        writer.writerow(report_data)