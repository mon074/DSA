nums =[1,0]
k=13
s=1
arr= nums.copy()
while s<len(nums):
    for i in range(0,len(nums)-s):
        arr[i] += nums[i+s]
        if arr[i]%k==0:
            print(True)
            break
    s+=1
else:
    print(False)