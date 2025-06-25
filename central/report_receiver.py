from flask import Flask, request, jsonify
from report_verifier import verify_report_integrity
from report_db import save_report_metadata
import os

app = Flask(__name__)
REPORT_DIR = '/tmp/reports'
os.makedirs(REPORT_DIR, exist_ok=True)

@app.route('/upload', methods=['POST'])
def receive_report():
    file = request.files['report']
    expected_hash = request.form.get('hash')

    filename = file.filename
    filepath = os.path.join(REPORT_DIR, filename)
    file.save(filepath)

    # 무결성 검증
    if not verify_report_integrity(filepath, expected_hash):
        return jsonify({'status': 'fail', 'reason': 'hash mismatch'}), 400

    # DB 저장
    save_report_metadata(filename, request.remote_addr, expected_hash)
    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(port=8000)
