n, m = map(int, input().split())



## DFS
visited_dfs = [False] * (n + 1)
result_dfs = []

def dfs(v, n, m):
    #print(result_dfs)
    if len(result_dfs) == m:
        print(' '.join(map(str, result_dfs)))
        return
    for i in range(1, n+1):
        if not visited_dfs[i] and result_dfs[-1] < i:
            visited_dfs[i] = True
            result_dfs.append(i)
            dfs(i, n, m)
            visited_dfs[i] = False
            result_dfs.pop()

for  i in range(1, n+1):
    visited_dfs[i] = True
    result_dfs = [i]
    dfs(i, n, m)
    visited_dfs = [False] * (n + 1)
    result_dfs = []