def solution(n):
    answer = -1
    num = pow(n, 0.5)

    if num == int(num):
        answer = int(pow(num + 1, 2))

    return answer
