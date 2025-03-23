from collections import deque

n, m = map(int, input().split())
l = []
for i in range(n):
    t = []
    for j in input():
        t.append(int(j))
    l.append(t)

visited = []
for i in range(n):
    t = []
    for j in range(m):
        t.append(0)
    visited.append(t)
    
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs():
    queue = deque([(0, 0, 1)])
    visited[0][0] = 1

    while queue:
        x, y, dist = queue.popleft()

        if x == n - 1 and y == m - 1:
            return dist

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m and l[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = 1
                queue.append((nx, ny, dist + 1))

    return -1

print(bfs())

'''
4 6
101111
101010
101011
111011
'''