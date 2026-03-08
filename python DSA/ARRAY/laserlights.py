bank=["1000001","1001010","0010000","0001111","0000000"]

r,arr,cell = 0,[],0
while r<len(bank):
    while cell < len(bank[0]):

        if bank[r][cell]=='1':
            arr.append([r,cell])
        cell+=1
    r+=1
    cell=0
print(arr)
i=0
j = i+1
count = 0
if arr == [] or arr[0][0] == arr[-1][0]:
    print(count)
else:
    while arr[i][0] < len(bank)-1 and j<len(arr):
        print(count)
        if arr[j][0]==arr[i][0]:
            j+=1
        else:
            if arr[j-1][0]==arr[i][0] or arr[j-1][0]==arr[j][0]:
                count +=1
                if j == len(arr)-1:
                    i+=1
                    j=i+1
                else:
                    j+=1
            else:
                i+=1
                j=i+1
print(count)

