def solution(s):
    s = list(s.split(' '))
    for i in range(len(s)):
        s[i] = int(s[i])
    answer = str(min(s))+' '+str(max(s))
    return answer


print(solution("-1 -2 -3 -4"))