n = int(input())
direct = list(map(int,input().split()))
time = list(map(int,input().split()))

t = 0
for i in range(n - 1, -1, -1):
    if i == n - 1:
        t = direct[i]
    else:
        t += direct[i + 1] - direct[i]
        print(direct[i] - direct[i - 1])
    if time[i] > t:
        print(time[i], t, time[i] - t, "----------")
        t += time[i] - t
        
    #t += direct[i] - direct[i - 1]
    
    print(direct[i], t)
print(t + direct[0])
'''
4
2 5 7 10
20 4 16 11

3
1 2 3
3 2 1



10 11
9 12
8 13
7 14
7 15
7 16
6 17
5 18
4 19
3 20
2 21
1 22
0 23

'''