N = int(input())
A = map(int, input().split())
l=list(A)
final1=0
final2=0
fin=[]
l1=l[0:int(len(l)/2)]
l2=l[int(len(l)/2):len(l)]

for i in l1:
    while i>10:
        i//=10
    fin.append(i)

for i in l2:
    i=i%10
    fin.append(i)

final=(''.join(str(x)for x in fin))

for i in range(0,len(final),2):
       final1+=int(final[i])
for i in range(1,len(final),2):
       final2+=int(final[i])

final=final1-final2
if final%11==0:
    print("OUI")
else:
    print("NON")
