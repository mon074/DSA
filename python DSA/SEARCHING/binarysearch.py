arr = [2,4,6,7,8,10,12,14]
num=9
start = 0
end = len(arr)-1

while start<=end:
    m = (end-start)//2 + start
    if arr[m] == num:
        print(num,"at index: ",m)
        break
    elif arr[m]<num:
        start = m+1
    else:
        end = m-1
else:
    print("Number is nowhere to be found!")