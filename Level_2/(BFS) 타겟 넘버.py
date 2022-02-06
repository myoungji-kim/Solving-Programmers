def solution(numbers, target):
    save = [0]
    for i in numbers:
        temp = []
        for j in save:
            temp.append(j+i)
            temp.append(j-i)
        save = temp
    return save.count(target)
