from itertools import permutations

result = []


def check_per(pList_one):
    num = int(pList_one)
    if num > 1:
        for k in range(2, num):
            if num % k == 0:
                return False
        result.append(num)
    else:
        return False


def solution(numbers):
    for i in range(1, len(numbers) + 1):
        pList = list(map(''.join, permutations(list(numbers), i)))

        for pList_one in pList:
            check_per(pList_one)

    return len(set(result))
