import sys
input = sys.stdin.readline

def f(n):
    L = [0] * 10
    length = len(str(n))
    #print(length)
    for i in range(length):
        factor = 10 ** i
        higher = n // (factor * 10)
        current = (n // factor) % 10
        lower = n % factor
        #print(factor, ':', current, higher, lower)
        for d in range(10):
            #print(d)
            if d < current:
                L[d] += (higher + 1) * factor
            elif d == current:
                L[d] += higher * factor + (lower + 1)
            else:
                L[d] += higher * factor
            
            #print(L)
        L[0] -= factor
        
    return L

'''
n = 1000000
n = 543212345
n = 455
n = 999
'''

n = int(input())
#print(n)
r = list(map(str,f(n)))
print(' '.join(r))

'''
543212345
'''