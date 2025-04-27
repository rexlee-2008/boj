
def solve(n, k):

    dp = [[0] * (n + 1) for _ in range(k + 1)]
    

    for i in range(n + 1):
        dp[1][i] = 1


    for i in range(2, k + 1):
        for j in range(n + 1):
            dp[i][j] = dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]
            dp[i][j] %= 1000000000

    return dp[k][n]


n, k = map(int, input().split())
print(solve(n, k))