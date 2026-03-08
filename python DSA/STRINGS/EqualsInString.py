
s='321881'
change = 1
n=len(s)
l= n*(n+1)//2-3
i=0
j=i+1
a=1

print(l)
while j < l:
    print(j)
    s = s + str((int(s[i])+int(s[j]))%10)

    if j==n-1:
        i=j+1
        j=i+1
        n+=(len(s)-change)
        change+=1

    else:
        i+=1
        j+=1
if s[-1]==s[-2]:
    print(True)
else:
    print(False)
print(s)
print(len(s))
