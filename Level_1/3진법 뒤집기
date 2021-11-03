def solution(n):
    save = []
    while True:
        save.append(n % 3)
        n //= 3
        if n == 0:
            break
    reverse = []
    for i in range(len(save)):
        reverse.append(save[i])

    reverse.reverse()

    for i in range(len(reverse)):
        reverse[i] *= 3 ** i

    return sum(reverse)


print(solution(125))
