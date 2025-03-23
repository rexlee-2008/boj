k = int(input())
num_list = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
inequality = input().split()
check = [False] * 10
answer = [0, 9999999999]
def backtrack(i, result):
    #print(result)
    if i == k + 1:
        if int(result) > int(answer[0]):
            answer[0] = result
        if int(result) < int(answer[1]):
            answer[1] = result
        #print(answer)
        #print(k, i, result)
        return
    for j in num_list:
        if not check[j]:
            if (inequality[i - 1] == '<' and int(result[-1]) < j) or (inequality[i - 1] == '>' and int(result[-1]) > j):
                #print(check, i, j)
                check[j] = True
                result += str(j)
                i += 1
                
                backtrack(i, result)
                
                check[j] = False
                result = result[:-1]
                i -= 1
                #print(result)
                
for i in range(9, -1, -1):
    check[i] = True
    backtrack(1, str(i))
    check = [False] * 10
#print(answer)
print(answer[0])
print(answer[1])
'''
2
< >

9
> < < < > > > < <
'''