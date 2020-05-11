a=list(input())
k=int(input())
n=k
while k>26:
    k=k-26
while n>9:
    n=n-10
for i in range(0,len(a)):
    if a[i].isupper():
        a[i]=chr(ord(a[i])+k)
        if not a[i].isupper():
            a[i]=chr(ord(a[i])-26)

    if a[i].islower():
        a[i]=chr(ord(a[i])+k)
        if not a[i].isalpha():
            a[i]=chr(ord(a[i])-26)
    if a[i].isdigit():
        a[i]=str(int(a[i])+n)
        if int(a[i])>=10:
            a[i]=str(int(a[i])-10)
print (''.join(a))
