import sys
sys.setrecursionlimit(10**7)
m, n=map(int,input().split())
l = []
direction = []
for i in range(n):
    t=list(map(int,input().split()))
    for j in range(len(t)):
        if t[j] == 1:
            direction.append([i, j])
    l.append(t)
#print(direction, l)
arr = [n - 1, m - 1]

def dfs(direction, days):
    New_direction = []
    days += 1
    for i in direction:
        x = i[0]
        y = i[1]
        #print(x, y)
        if x > 0:
            if l[x - 1][y] == 0:
                l[x - 1][y] = 1
                New_direction.append([x - 1, y])
        if x < arr[0]:
            if l[x + 1][y] == 0:
                l[x + 1][y] = 1
                New_direction.append([x + 1, y])
        if y > 0:
            if l[x][y - 1] == 0:
                l[x][y - 1] = 1
                New_direction.append([x, y - 1])
        if y < arr[1]:
            if l[x][y + 1] == 0:
                l[x][y + 1] = 1
                New_direction.append([x, y + 1])
        #print(New_direction)
    if len(New_direction) == 0:
        flag = 0
        #print(l)
        for i in l:
            for j in i:
                if j == 0:
                    print("----------------------", -1)
                    flag = 1
                    break
        print(flag)
        if flag == 0:
            print("----------------", days - 1)
        return 0
    dfs(New_direction, days)
dfs(direction, 0)
#print(l)
        
            
            
            
            
            
'''
2 2
0 0
0 0

6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
'''