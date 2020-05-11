'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
command=input()
x,y=0,0
for i in range(0,len(command)):
    a=command[i]
    if a=='L':
        x-=1
    if a=='R':
        x+=1
    if a=='U':
        y+=1
    if a=='D':
        y-=1
print (x,y)
