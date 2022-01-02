def solution(s):
    if len(s) == 4 or len(s) == 6:
        return True if s.isdigit() else False
    else:
        return False
