# bank=["1000001","1001010","0010000","0001111","0000000"]
# bank=["011001","000000","010100","001000"]
bank=["000","111","000"]

arr = []
r,cell=0,0

while r<len(bank):
    el=0
    if int(bank[r]) ==0:
        r +=1
        continue
    else:
        while cell < len(bank[0]):
            if bank[r][cell]=='1':
                el+=1
            cell+=1
        arr.append(el)
    r+=1
    cell=0

i=0
j=i+1
count =0

while j<len(arr):
    count += arr[i]*arr[j]
    i+=1
    j+=1

print(count)