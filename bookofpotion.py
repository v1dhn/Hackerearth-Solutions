x=0
a=list(input())
if len(a)!=10:
    print ("Illegal ISBN")
else:
    for i in range(1,len(a)+1):
        x+=i*int(a[i-1])
    if (x%11==0):
        print ("Legal ISBN")
    else:
        print("Illegal ISBN")
        
