def solution(s):
    if s[0] == ")" or s[-1] == "(":
        return False

    open, close = 0, 0

    for i in range(len(s)):
        if s[i] == "(":
            open += 1
        elif s[i] == ")":
            close += 1
            if close > open:
                return False

    if open == close:
        return True
    else:
        return False

print(solution("())(()"))