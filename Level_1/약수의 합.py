def solution(n):
    answer = []
    for i in range(1, n//2 + 1): # n + 1까지 돌 필요가 없음
        if n % i == 0:
            answer.append(i)
    answer = sum(set(answer))
    return answer + n
