def test(m):
    save = ''
    while True:
        save += str(m % 2)
        m //= 2
        if m == 0:
            break
    return save.count('1')

def solution(n):
    first = test(n)
    second = n + 1
    while True:
        result = test(second)
        if result == first:
            break
        else:
            second += 1
    return second


print(solution(15))