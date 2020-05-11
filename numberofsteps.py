T = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
n = min(A)
count = 0
for i in range(0,T):
    while (A[i] != n and A[i] > n and B[i] != 0):
        A[i] = A[i] - B[i]
        count += 1
if A.count(A[0]) == len(A):
    print(count)
else:
    print("-1")
