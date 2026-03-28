nums = [10,3,1,1]

min0 = nums[0]
min1 = nums[1]
min2 = nums[2]

for i in range(2,len(nums)):

    if min1>=nums[i]:

        min2 = min1
        min1 = nums[i]

print(min0+min1+min2)
