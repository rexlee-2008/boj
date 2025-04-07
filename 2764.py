import math

def f(p):
    n = sum(p)
    t = []
    
    for i, r in enumerate(p):
        t.append([(i, j) for j in range(r)])

    def h(x, y):
        c1 = 0
        r, c2 = x, y
        while c2 < len(t[r]):
            c1 += 1
            c2 += 1
        r, c2 = x, y
        while r < len(t) and c2 < len(t[r]):
            c1 += 1
            r += 1
        return c1 - 1
    
    d = []
    for x in range(len(t)):
        for y in range(len(t[x])):
            d.append(h(x, y))
    #print()
    #for i in d:
        #print(i)
    #print()
    return math.factorial(n) // math.prod(d)

a = int(input())
for i in range(a):
    b = input()
    p = list(map(int,input().split()))
    #print(p)
    print(f(p))

'''
6
1
30
5
1 1 1 1 1
3
3 2 1
4
5 3 3 1
5
6 5 4 3 2
2
15 15
'''








