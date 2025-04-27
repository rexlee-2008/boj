from math import isqrt

def mobius(n):
    p = 0
    i = 2
    while i * i <= n:
        if n % (i * i) == 0:
            return 0
        if n % i == 0:
            p += 1
            n //= i
        i += 1
    if n > 1:
        p += 1


    if p % 2:
        return -1
    else:
        return 1

def count_squarefree(x):
    result = 0
    for i in range(1, isqrt(x) + 1):
        mu = mobius(i)
        if mu != 0:
            result += mu * (x // (i * i))
    return result


k = int(input())

left = 1
right = 2 * k
while left < right:
    mid = (left + right) // 2
    if count_squarefree(mid) < k:
        left = mid + 1
    else:
        right = mid

print(left)