from collections import deque
n, m, k = map(int, input().split())
maze = []

for i in range(n):
    temp = []
    for j in input():
        temp.append(j)
    maze.append(temp)

maze[n-1][0] = "T"

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
#visited_dfs = [[False] * m for _ in range(n)]
num = 0

def dfs(vx, vy, ex, ey, count, k):
    global num
    #visited_dfs[vx][vy] = True
    for i in range(4):
        x = vx + dx[i]
        y = vy + dy[i]
        #print(x, y, vx, vy, i)
        #if x == 0 and y == m-2:
            #print(x, y)
            #print(maze)
        
        if vx == ex and vy == ey:
            if count == k:
                maze[vx][vy] = "T"
                #print(count, ex, ey, num)
                #for j in maze:
                    #print(j)
                maze[vx][vy] = "."
                num += 1
            return
        if 0 <= x <= n-1 and 0 <= y <= m-1 and maze[x][y] == '.':
            maze[x][y] = "T"
            dfs(x, y, ex, ey, count + 1, k)
            maze[x][y] = "."
    return
dfs(n-1, 0, 0, m-1, 1, k)

print(num)

'''
3 4 6
....
.T..
....


34510
2T69
1.78
'''