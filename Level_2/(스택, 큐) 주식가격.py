from collections import deque


def solution(prices):
    q = deque(prices)
    answer = []
    while len(q) != 0:
        cnt = 0
        num = q.popleft()
        for i in q:
            cnt += 1
            if num > i:
                break
        answer.append(cnt)
    return answer
