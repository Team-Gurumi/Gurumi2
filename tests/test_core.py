import os
from node.core.container_executor import execute_task

def test_container_execution_creates_result_file(tmp_path):
    # 테스트용 디렉토리와 input 파일 생성
    task_dir = tmp_path
    input_file = task_dir / "input.txt"
    script_file = task_dir / "run.sh"

    input_file.write_text("hello")
    script_file.write_text("#!/bin/bash\ncat input.txt | tr a-z A-Z > result.txt")
    os.chmod(script_file, 0o755)

    # 테스트 대상 함수 실행
    execute_task(str(task_dir))

    # 실행 결과 확인
    result_path = task_dir / "result.txt"
    assert result_path.exists()
    assert result_path.read_text().strip() == "HELLO"
