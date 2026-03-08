# nums = [3,5,2,3]
# nums = [3,5,4,2,4,6]
nums = [4,1,5,1,2,5,1,5,5,4]

nums.sort()

l = 0
r =  len(nums)-1
mm = 0
while l<r:

    sum = nums[l]+nums[r]

    if sum > mm:
        mm = sum
    
    l+=1
    r-=1

print(mm)


# print(nums)
