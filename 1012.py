import sys
sys.setrecursionlimit(10**8)
t = int(input())


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for p in range(t):
    b, a, k = map(int,input().split())

    maps = [[0] * b for _ in range(a)]
    for i in range(k):
        y, x = map(int,input().split())
        maps[x][y] = 1
    #print(maps)

    def dfs(x, y, num):
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= a or ny < 0 or ny >= b:
                continue
            if maps[nx][ny] == 1:
                #print(nx, ny, "----------")
                maps[nx][ny] = 0
                dfs(nx, ny, num+1)
        #if flag == 0:
            #print(num)
        #for i in map:
            #print(i)
        #print(num)
        return

    arr =  []        
    count = 0
    #for i in maps:
        #print(i)

    for i in range(a):
        for j in range(b):
            if maps[i][j] == 1:
                #print("___________________")
                #for q in maps:
                    #print(q)
                count += 1
                maps[i][j] = 0
                dfs(i, j, 1)
                #for k in map:
                    #print(k)
                #print("--------------------------------")
    print(count)
'''
2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5
'''