'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
flag=True
a=int(input())
b=input()[:a]
for i in range(0,a-1):
    if b[i]==b[i+1]=='H':
        flag=False
if flag==False:
    print('NO')
else:
    print ('YES')
    b=b.replace('.','B')
    print (b)

