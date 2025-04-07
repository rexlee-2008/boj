n = int(input())
arr = list(map(int, input().split()))


lis = []

temp = [-1] * n

l = [-1] * n

for i in range(n):
    pos = 0
    for j in range(len(lis)):
        if lis[j] >= arr[i]:
            pos = j
            break
    else:
        pos = len(lis)
    
    if pos < len(lis):
        lis[pos] = arr[i]
    else:
        lis.append(arr[i])
    
    temp[pos] = i
    if pos > 0:
        l[i] = temp[pos - 1]


for i in lis:
    print(i,end=" ")

'''
result = []
index = lis_indices[length - 1]
while index != -1:
    result.append(arr[index])
    index = prev_indices[index]

print(' '.join(map(str, result[::-1])))
'''

'''
6
10 20 10 30 20 50
'''