temp = ["+", "-", "*", "/"]
n=int(input())
l = list(map(int,input().split()))
d = list(map(int,input().split()))
arr = []
for i in range(4):
    if d[i] != 0:
        for j in range(d[i]):
            arr.append(temp[i])
#print(arr)

arr_len = len(arr)
visited_dfs = [False] * (arr_len + 1)
result_dfs = []
max_result = -1000000001
min_result = 1000000001
def dfs(v, n, m):
    #print(result_dfs)
    global max_result
    global min_result
    #print(result_dfs)
    if len(result_dfs) == n - 1:
        print(result_dfs)
        num = l[0]
        for i in range(n - 1):
            if result_dfs[i] == "/" and l[i + 1] == 0:
                num = 0
                return
            if result_dfs[i] == "+":
                num += l[i + 1]
            elif result_dfs[i] == "-":
                num -= l[i + 1]
            elif result_dfs[i] == "*":
                num *= l[i + 1]
            else:
                num /= l[i + 1]
            num = int(num)
        #num = result_dfs[i] + str(l[i + 1])
        #print(num)
        if num > max_result:
            max_result = num
        if num < min_result:
            min_result = num
        
        
        return
    for i in range(m):
        if visited_dfs[i] == False:
            visited_dfs[i] = True
            result_dfs.append(arr[i])
            dfs(i, n, m)
            visited_dfs[i] = False
            result_dfs.pop()

for i in range(arr_len):
    #print(i)
    visited_dfs[i] = True
    result_dfs = [arr[i]]
    dfs(i, n, arr_len)
    #print("----")
    visited_dfs = [False] * (arr_len + 1)
    result_dfs = []
print(int(max_result))
print(int(min_result))
'''
2
1 2
1 0 0 0

5
1 2 3 4 5
1 1 1 1
'''