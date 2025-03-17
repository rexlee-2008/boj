a=input()
b=input()
l=[]
m=0
x=0
y=0
for i in range(len(a)):
    l.append([0]*len(b))
for i in range(len(a)):
    for j in range(len(b)):
        if a[i]==b[j]:
            if i==0 or j==0:
                l[i][j]=1
            else:
                l[i][j]=l[i-1][j-1]+1
            if l[i][j]>m:
                m=l[i][j]
                x=i
                y=j
x=x-m+1
for i in range(m):
    print(a[x],end='')
    x+=1
print()
print(m)
  
'''
yeshowmuchiloveyoumydearmotherreallyicannotbelieveit
yeaphowmuchiloveyoumydearmother
'''