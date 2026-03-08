arr1 = [5,7,7,8,8,10]
target = 7
res =[]

#binary search algorithm
def BinarySearch(arr,low,high,x):
    while low<=high:
        mid = low + (high-low)//2
        if arr[mid] == x:
            return mid
        elif arr[mid]<x:
            low = mid +1
        else:
            high = mid - 1
    
    return -1
result = BinarySearch(arr1,0,len(arr1)-1,target)
if result == -1:
    print("Target not found!")
else:
    print("Target found at index",result)



