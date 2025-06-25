def accept_task(request_data):
    # 예시 정책: task_priority가 1 이상이면 수락
    if request_data.get('task_priority', 0) >= 1:
        print("[정책 판단] 요청 수락")
        return True
    else:
        print("[정책 판단] 요청 거절")
        return False