s = "3902"
change = 0
n=len(s)
l= n*(n-1)//2-1
i=0
j=i+1
# a=1

while j <=l+1:
    s = s + str((int(s[i])+int(s[j]))%10)
    if j==n-1+change:
        i=j+1
        j=i+1
        change=n-1
        # a+=1
    else:
        i+=1
        j+=1
if s[-1]==s[-2]:
    print(True)
else:
    print(False)
print(s)
print(len(s))