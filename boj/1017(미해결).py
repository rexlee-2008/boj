def prime(n):
    if n%2==0 and n!=2:
        return 0
    a = 1
    for i in range(3, int(n**0.5)+1, 2):
        if n%i==0:
            a = 0
            break
    return a
n=int(input())
l=list(map(int,input().split()))
d=[]
count=0
for i in range(len(l)):
    for j in range(i+1,len(l)):
        #print(l[i],l[j])
        if l[i]+l[j] in d:
            count+=1
            continue
        elif prime(l[i]+l[j])==1:
            d.append(l[i]+l[j])
            count+=1
print(d,count)

'''
6
1 4 7 10 11 12
'''