n, m = map(int,input().split())
v = [0] * n
w = [0] * n
dp = [[0] * (m + 1) for _ in range(n)]
for i in range(n):
    x = list(map(int,input().split()))
    w[i] = x[0]
    v[i] = x[1]
#print(w, v, dp)

for i in range(n):
    for j in range(1, m + 1):
        if j > w[i] - 1:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i]] + v[i])
            if dp[i - 1][j - w[i]] == v[i]:
                #print("------------------")
                dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = dp[i - 1][j]
            
        #for k in dp:
            #print(k)
print(dp[n-1][m])
#print(dp)

'''
4 7
6 13
4 8
3 6
5 12

3 5
2 3
3 2
5 4

4 7
1 7
2 2
3 3
4 4

1 13
2 5
'''