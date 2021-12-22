# 풀이 1
def solution(n):
    answer = '수'
    for i in range(2, n + 1):
        if i % 2 == 0:
            answer += '박'
        else:
            answer += '수'
    return answer

# 풀이 2
def solution(n):
    answer = '수'
    for i in range(2, n + 1):
        answer = answer + '박' if i % 2 == 0 else answer + '수'
    return answer
