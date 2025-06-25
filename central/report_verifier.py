import hashlib

def verify_report_integrity(report_path, expected_hash):
    """SHA-256 해시로 무결성 검증"""
    sha256 = hashlib.sha256()
    with open(report_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            sha256.update(chunk)
    actual_hash = sha256.hexdigest()
    return actual_hash == expected_hash
