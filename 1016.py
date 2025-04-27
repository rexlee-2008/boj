n, m = map(int,input().split())
diff = m - n + 1
arr = [0] * (diff)
square = int(m ** .5) + 1

for j in range(2, square):
    #print(j)
    sq = j * j
    #print(((n + sq - 1) // sq) * sq)
    for i in range(((n + sq - 1) // sq) * sq, m + 1, sq):
        #print(i, j)
        arr[i - n] = 1
#print(arr)
print(arr.count(0))


'''
1089 1089
'''