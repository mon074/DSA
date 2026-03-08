blocks = "WBWBBBW"
k = 2

l=0
r=0
m=200
ops=0
while r<len(blocks):
    if r<k:
        if blocks[r]=='W':
            ops+=1
        r+=1
    else:
        if blocks[l]=="W":
            ops-=1
        l+=1
        if blocks[r]=="W":
            ops+=1
        r+=1
    if r>=k:
        m=min(ops,m)
        if m==0:
            return m
else:
    print(m)
    


