from collections import deque
import sys
input = sys.stdin.read

data = input().split()
m, n = int(data[0]), int(data[1])
l = []
queue = deque()
index = 2

for i in range(n):
    t = []
    for j in range(m):
        t.append(int(data[index]))
        if t[-1] == 1:
            queue.append((i, j))
        index += 1
    l.append(t)

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs():
    days = -1
    while queue:
        days += 1
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and l[nx][ny] == 0:
                    l[nx][ny] = 1
                    queue.append((nx, ny))
    
    for row in l:
        if 0 in row:
            return -1
    return days

print(bfs())

'''
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
'''