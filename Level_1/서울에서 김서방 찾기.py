def solution(seoul):
    for i in range(len(seoul)):
        if "Kim" == seoul[i]:
            answer = "김서방은 {}에 있다".format(i)
            break

    return answer
