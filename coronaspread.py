case=0
count=int(input())
for i in range(0,count):
    test=int(input())
    l=list(map(int,input().split()))
    for i in range(1,len(l)):
        if l[i]-l[i-1]<=2:
            case=case+1
