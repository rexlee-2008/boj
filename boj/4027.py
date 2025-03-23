n=int(input())
l=[1,3,9,27,81,243,729]
d=[0]
for i in l:
    a=d.copy()
    for j in d:
        a.append(j+i)
        a.append(j-i)
        print(a)
    d=a.copy()
    set(d)
    print(a)