def solution(answers):
    winner = []
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    x = y = z = score_1 = score_2 = score_3 = 0

    for i in range(len(answers)):
        if answers[i] == first[x]:
            score_1 += 1

        if answers[i] == second[y]:
            score_2 += 1

        if answers[i] == third[z]:
            score_3 += 1

        x = 0 if x == 4 else x + 1
        y = 0 if y == 7 else y + 1
        z = 0 if z == 9 else z + 1

    temp = [score_1, score_2, score_3]

    if score_1 == max(temp):
        winner.append(1)
    if score_2 == max(temp):
        winner.append(2)
    if score_3 == max(temp):
        winner.append(3)

    return winner
