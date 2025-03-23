m, n = map(int, input().split())

arr = set(input().split())
arr = list(arr)
arr.sort()
#print(arr)

## DFS
visited_dfs = [False] * 123
result_dfs = []

def dfs(n, m, vowel, consonant):
    #print(result_dfs)
    if len(result_dfs) == m and vowel > 0 and consonant > 1:
        print(''.join(map(str, result_dfs)))
        return
    for j in arr:
        i = ord(j)
        if not visited_dfs[i] and ord(result_dfs[-1]) < i:
            visited_dfs[i] = True
            result_dfs.append(chr(i))
            if chr(i) == 'a' or chr(i) == 'e' or chr(i) == 'i' or chr(i) == 'o' or chr(i) == 'u':
                dfs(n, m, vowel + 1, consonant)
            else:
                dfs(n, m, vowel, consonant + 1)
            visited_dfs[i] = False
            result_dfs.pop()

for j in arr:
    i = ord(j)
    visited_dfs[i] = True
    result_dfs = [chr(i)]
    if chr(i) == 'a' or chr(i) == 'e' or chr(i) == 'i' or chr(i) == 'o' or chr(i) == 'u':
        dfs(n, m, 1, 0)
    else:
        dfs(n, m, 0, 1)
    visited_dfs = [False] * 123
    result_dfs = []

'''
4 6
a t c i s w

3 6
a b c d e f
'''