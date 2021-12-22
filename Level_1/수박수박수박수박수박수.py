def solution(n):
    answer = '수'
    for i in range(2, n + 1):
        if i % 2 == 0:
            answer += '박'
        else:
            answer += '수'
    return answer
