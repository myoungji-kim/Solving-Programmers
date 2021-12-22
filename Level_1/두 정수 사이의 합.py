def solution(a, b):
    if b < a:
        temp = b
        b = a
        a = temp

    answer = 0
    print(a, b)
    for i in range(a, b + 1):
        answer += i
    return answer
