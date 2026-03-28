arr = [4,2,1,3]
arr = [-17,46,63,81,-101,-91,121,-2,112,-15,-65,-96,6,-139]


arr.sort()
print(arr)
i=0
j=i+1
ans = [0]
min = float('inf')
flag=1

while j<len(arr):

    if arr[j]-arr[i] < min:
        min = arr[j]-arr[i]

        for freq in range(flag):
            ans.pop()

        ans.append([arr[i],arr[j]])
        flag = 1
        
    
    elif arr[j]-arr[i] == min:
        ans.append([arr[i],arr[j]])
        flag+=1

    # for i in range(len(ans),-1,-1):


    i+=1
    j+=1

print(ans)

