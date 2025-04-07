n, m = map(int, input().split())
l = [input().strip() for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

max_num = 0

def dfs(vx, vy, visited, count):
    global max_num
    max_num = max(max_num, count)
    
    for i in range(4):
        tx = vx + dx[i]
        ty = vy + dy[i]
        
        if 0 <= tx < n and 0 <= ty < m:
            s = ord(l[tx][ty]) - ord('A')
            if not visited[s]:
                visited[s] = True
                dfs(tx, ty, visited, count + 1)
                visited[s] = False

visited = [False] * 26
v = ord(l[0][0]) - ord('A')
visited[v] = True

dfs(0, 0, visited, 1)

print(max_num)