input()
a=1
m=10**9+7
n=list(map(int,input().split()))
for i in n:
    a=(a*i)%m
print (a)
