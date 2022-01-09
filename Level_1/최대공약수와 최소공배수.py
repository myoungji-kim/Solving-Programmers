def gcd(n, m):
    while (m):
        n, m = m, n % m
    return n
    
def lcm(n, m, gcdNum):
    return (n * m) // gcdNum

def solution(n, m):
    answer = []
    gcdNum = gcd(n, m)
    answer.append(gcdNum)
    answer.append(lcm(n, m, gcdNum))
    return answer
