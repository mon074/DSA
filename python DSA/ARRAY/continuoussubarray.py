nums =[23,2,6,4,7]
k=13
l=0

while l<len(nums)-1:
    r=l+1
    sum=nums[l]

    while r<len(nums):
        sum+= nums[r]
        if sum%k==0:
            print(True)
        r+=1
    l+=1
else:
    print(False)