def solution(a, b):
    lastDay = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    name = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    month = 0
    for i in range(a - 1):
        month += lastDay[i]
    month += b - 1

    answer = name[month % 7]
    return answer


print(solution(5, 24))
