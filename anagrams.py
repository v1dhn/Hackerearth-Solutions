from collections import Counter
count=int(input())
for i in range(count):
    ina=input()
    inb=input()
    a=Counter(ina)
    b=Counter(inb)
    common=list((a&b).elements())
    rem=len(ina)+len(inb)-2*len(common)
    print(rem)
