n, m = map(int, input().split())
v = []
w = []
dp = [0] * (m + 1)

for i in range(n):
    x = list(map(int, input().split()))
    count = x[2]
    weight = x[0]
    value = x[1]

    power = 1
    while count > 0:
        min_num = min(power, count)
        w.append(weight * min_num)
        v.append(value * min_num)
        count -= min_num
        power *= 2


#print(dp, w, power)
for i in range(len(w)):
    for j in range(m, w[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - w[i]] + v[i])
#print(dp, w, v, weight, value, count, power)
print(max(dp))

'''
2 3
2 7 1
1 9 3

3 9
8 5 1
1 2 2
9 4 1
'''