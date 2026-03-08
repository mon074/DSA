# bank=["1000001","1001010","0010000","0001111","0000000"]
# bank=["011001","000000","010100","001000"]
bank=["000","111","000"]
d = dict()

r,cell = 0,0

while r < len(bank):
    d[r]=0
    while cell <len(bank[0]):
        if bank[r][cell]=='1':
            d[r]+=1
        cell+=1
    r+=1
    cell=0
print(d)

i=0
j=i+1
count=0

while i<len(d)-1 and j<len(d):
    if d[j] !=0:
        count += d[i]*d[j]
        i+=1
        j=i+1
    else:
        j+=1

print(count)
