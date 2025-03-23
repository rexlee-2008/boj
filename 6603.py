while True:
    temp = list(map(int,input().split()))
    num_list = temp[1:]
    k = temp[0]
    if k == 0:
        exit()
    visited_dfs = [False] * (50)
    result_dfs = []

    def dfs(n):
        #print(result_dfs)
        if len(result_dfs) == 6:
            print(' '.join(map(str, result_dfs)))
            return
        for i in num_list:
            if not visited_dfs[i] and result_dfs[-1] < i:
                visited_dfs[i] = True
                result_dfs.append(i)
                dfs(n)
                visited_dfs[i] = False
                result_dfs.pop()

    for i in num_list:
        visited_dfs[i] = True
        result_dfs = [i]
        #print(visited_dfs, result_dfs)
        dfs(k)
        visited_dfs = [False] * (50)
        result_dfs = []
    print()
'''
7 1 2 3 4 5 6 7
8 1 2 3 5 8 13 21 34
0
'''