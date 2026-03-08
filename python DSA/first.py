arr1 = [5,7,7,8,8,10]
target = 7
res =[]

#binary search algorithm
def BinarySearch(arr,low,high,x):
    while low<=high:
        mid = low + (high-low)//2
        if arr[mid] == x:
            while low<=high:
               if arr[low]!=target:
                 low = low+1
               else:
                  res.append(low)
                  low = low +1
            return res        
        elif arr[mid]<x:
            low = mid +1
        else:
            high = mid - 1
    res.append(-1)
    res.append(-1)
    return res
'''result = BinarySearch(arr1,0,len(arr1)-1,target)
if result == -1:
    print("Target not found!")
else:
    print("Target found at index",result)'''

result = BinarySearch(arr1,0,len(arr1)-1,target)
print(result)

