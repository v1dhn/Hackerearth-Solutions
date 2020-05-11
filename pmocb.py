def prime(x):
	for i in range(2,x):
		if x%i==0:
			return x;
	
count=int(input())
tot=0
l=[]
for i in range(count):
	a,b=map(int,input().split())
	for j in range(a,b):
		prime(j)
