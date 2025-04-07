from collections import deque

def bfs(n, k):
    max_num = 100001
    visited = [-1] * max_num
    queue = deque([n])
    visited[n] = 0

    while queue:
        #print(queue)
        #print(visited)
        x = queue.popleft()
        
        if x == k:
            return visited[x]
        
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx < max_num and visited[nx] == -1:
                visited[nx] = visited[x] + 1
                queue.append(nx)
    return

n, m = map(int, input().split())
graph = [list(map(int,input().strip())) for _ in range(n)]

print(graph)

'''
6 4
0100
1110
1000
0000
0111
0000
'''