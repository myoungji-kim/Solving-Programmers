def solution(n):
    ls = [0, 1]
    for i in range(2, n + 1):
        ls.append(ls[i - 2] + ls[i - 1])
    answer = ls[n] % 1234567
    return answer


print(solution(5))
