from collections import deque
n, m, v = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)}

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for key in graph.keys():
    graph[key].sort()

## DFS
visited_dfs = [False] * (n + 1)
result_dfs = []

def dfs(v):
    visited_dfs[v] = True
    result_dfs.append(v)
    for i in graph[v]:
        if not visited_dfs[i]:
            dfs(i)

dfs(v)

## BFS
visited_bfs = [False] * (n + 1)
result_bfs = []

def bfs(v):
    visited_bfs[v] = True
    queue = deque([v])
    while queue:
        v = queue.popleft()
        result_bfs.append(v)
        for i in graph[v]:
            if not visited_bfs[i]:
                visited_bfs[i] = True
                queue.append(i)

bfs(v)

## Print DFS and BFS
for i in result_dfs:
    print(i, end=" ")
print()

for i in result_bfs:
    print(i, end=" ")
print()