from collections import deque
import copy

def bfs(x, y, color, maze, visited):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        cx, cy = queue.popleft()
        print(cx, cy, queue)
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and maze[nx][ny] == color:
                visited[nx][ny] = True
                queue.append((nx, ny))

n = int(input())
maze1 = [list(input().strip()) for _ in range(n)]
maze2 = copy.deepcopy(maze1)
for i in range(n):
    for j in range(n):
        if maze1[i][j] == "G":
            maze2[i][j] = "R"


print(maze1, maze2)

# 적록색약 X
visited1 = [[False] * n for _ in range(n)]
count1 = 0
for i in range(n):
    for j in range(n):
        if not visited1[i][j]:
            bfs(i, j, maze1[i][j], maze1, visited1)
            count1 += 1

# 적록색약 O
visited2 = [[False] * n for _ in range(n)]
count2 = 0
for i in range(n):
    for j in range(n):
        if not visited2[i][j]:
            bfs(i, j, maze2[i][j], maze2, visited2)
            count2 += 1

print(count1, count2)

'''
5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
'''