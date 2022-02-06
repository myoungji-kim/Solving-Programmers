def solution(n, arr1, arr2):
    a1, a2 = [], []
    dp = [[' ' for i in range(n)] for j in range(n)]

    for i in range(n):
        x, y = format(arr1[i], 'b'), format(arr2[i], 'b')
        while len(x) < n: x = '0' + x
        while len(y) < n: y = '0' + y
        a1.append(x)
        a2.append(y)
    for i in range(n):
        for j in range(len(a1)):
            if a1[i][j] == '1' or a2[i][j] == '1':
                dp[i][j] = '#'
        dp[i] = ''.join(dp[i])
    return dp
