v='aeiouAEIOU'
count=int(input())
for i in range(count):
    a=input()
    ans=0
    for i in a:
        if i in v:
            ans= ans + (a.index(i)+1)*(len(a)-a.index(i))
    print(ans)
