s=list(input())
for i in range(0,len(s)):
    if s[i].isupper():
        s[i]=s[i].lower()
    else:
        s[i]=s[i].upper()
s=''.join(s)
    
