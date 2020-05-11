'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
flag=True
a=input()
b=input()
l=list(b)
for i in range(0,len(l)-1):
    if l[i]==l[i+1]=='H':
        flag=False
if flag==False:
    print(NO)
else:
    for i in range(0,len(l)):
        if l[i]=='.':
            l[i]='B'

