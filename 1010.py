k = int(input())
for j in range(k):
    m, n = map(int, input().split())
    a = 1
    b = 1
    for i in range(m):
        a *= (n - i)
        b *= (m - i)
        #print(a, b)
    print(a // b)