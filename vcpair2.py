t = int (input ())
vowels = 'aeiou'
for i in range(t):
    c = 0
    n = int (input ())
    s = input ()

    for j in range (0,n-1):
        if (s[j] not in vowels) and (s[j + 1] in vowels):
            c+= 1
    print (c)
