numRows = 7

ans = []
for i in range(1,numRows+1):
    arr = []
    j=1
    while j < i+1:
        if j ==1:
            arr.append(1)
            j+=1
        elif j == i:
            arr.append(1)
            j+=1
        else:
            arr = arr + next
            j += len(next)
    ans.append(arr)
    next = []
    n=0
    while n+1 < len(arr):
        next.append(arr[n]+arr[n+1])
        n+=1
print(ans)     

