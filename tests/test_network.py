import requests
import tarfile
import os

def test_task_api_returns_result(tmp_path):
    # 테스트용 task 생성 및 압축
    task_dir = tmp_path / "task"
    task_dir.mkdir()
    (task_dir / "input.txt").write_text("abc")
    (task_dir / "run.sh").write_text("#!/bin/bash\ncat input.txt > result.txt")
    os.chmod(task_dir / "run.sh", 0o755)

    tgz_path = tmp_path / "job.tgz"
    with tarfile.open(tgz_path, "w:gz") as tar:
        tar.add(task_dir, arcname='.')

    # 서버가 이미 127.0.0.1:5000 에서 실행 중이라고 가정
    with open(tgz_path, 'rb') as f:
        res = requests.post("http://127.0.0.1:5000/run", files={'job': f})

    assert res.status_code == 200
    result_file = tmp_path / "result.tar.gz"
    result_file.write_bytes(res.content)

    with tarfile.open(result_file) as tar:
        tar.extractall(path=tmp_path)

    assert (tmp_path / "result.txt").read_text().strip() == "abc"
