nums =[23,2,6,4,7]
k=13

win=1
while win<len(nums):
    l=0
    r=l+1
    sum=nums[0]

    while r<len(nums):
        if r-l<=win:
            sum+=nums[r]
        else:
            sum-=nums[l]
            sum+=nums[r]
            l+=1
        if sum%k==0:
            print(True)
        r+=1
    win+=1
else:
    print(False)