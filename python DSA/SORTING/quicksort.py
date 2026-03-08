
arr = [10, 7, 8, 9, 1, 5]
start=0
end=len(arr)-1


def partition(start,end):
    pivot = arr[end]

    index = start-1

    for j in range(start,end):

        if arr[j]<=pivot:
            index+=1
            arr[index],arr[j]=arr[j],arr[index]

    arr[index+1],arr[end]=arr[end],arr[index+1]
    return index+1

def QuickSort(arr,start,end):
    if start<end:

        pi = partition(start,end)

        QuickSort(arr,start,pi-1)
        QuickSort(arr,pi+1,end)


QuickSort(arr,start,end)

print(arr)