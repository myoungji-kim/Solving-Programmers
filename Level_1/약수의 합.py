# 1
# 시간 복잡도 1/2 * n
def solution(n):
    answer = []
    for i in range(1, n//2 + 1): # n + 1까지 돌 필요가 없음
        if n % i == 0:
            answer.append(i)
    answer = sum(set(answer))
    return answer + n

# 2
# 시간 복잡도 n ** 0.5
def solution(n):
    answer = 0
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            if i != n//i:
                answer += (i+n//i)
            else:
                answer += i
    return answer
