arr = [64,22,25,12,11,12]


for start in range(len(arr)):
    m = arr[start]
    pos = start
    for i in range(start+1, len(arr)):
        if arr[i]<m:
            min = arr[i]
            pos = i
    if pos!=start:
        arr[pos],arr[start]=arr[start],arr[pos]
print(arr)