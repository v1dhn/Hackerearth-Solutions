l1=[]
l2=[]
t=int(input())
for i in range(t):
    price=0
    g,p=map(int,input().split())
    num=int(input())
    for j in range(num):
        ng,np=map(int,input().split())
        l1.append(ng)
        l2.append(np)
    if l1>l2:
        for i in l1:
            price=i*min(g,p)
    else:
        for i in l2:
            price+=i*max(g,p)
    print (price)
