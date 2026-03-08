arr = [5, 1, 8, 4, 2, 8,8]

for n in range(len(arr)):

    for j in range(1,len(arr)-n):

        if arr[j-1]>arr[j]:
            arr[j-1],arr[j]=arr[j],arr[j-1]
        
print(arr)


