# mutual_cloud/central/report_verifier.py
import hashlib

# 간단한 무결성 검증 (해시 비교)
def verify_report_integrity(report):
    report_copy = report.copy()
    received_hash = report_copy.pop('hash', None)

    if received_hash is None:
        return False

    sorted_items = sorted(report_copy.items())
    report_string = ''.join(f'{key}:{value}' for key, value in sorted_items)
    calculated_hash = hashlib.sha256(report_string.encode()).hexdigest()

    return received_hash == calculated_hash
