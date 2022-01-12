import math
from collections import deque


def solution(progresses, speeds):
    answer, qp, qs = [], deque(progresses), deque(speeds)
    while len(qp) != 0:
        cnt = 0
        temp = math.ceil((100 - qp[0]) / qs[0])

        for i, j in zip(list(qp), list(qs)):
            if i < 100:
                i += j * temp

            if i >= 100:
                qp.popleft()
                qs.popleft()
                cnt += 1
            else:
                break
        if cnt != 0:
            answer.append(cnt)
    return answer
