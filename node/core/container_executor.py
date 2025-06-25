# node/core/container_executor.py

import subprocess

def execute_in_container(task_data):
    print("[ContainerExecutor] 작업 실행 중... (모의 실행)")

    # 실제로는 Kata Container를 여기서 실행해야 함.
    # 지금은 임시로 로컬 명령어 실행
    try:
        result = subprocess.check_output(['python', '-c', task_data], stderr=subprocess.STDOUT)
        result = result.decode()
    except subprocess.CalledProcessError as e:
        result = e.output.decode()

    print("[ContainerExecutor] 작업 실행 완료.")
    return result
