nums = [90]
k=1

nums.sort()
i = 0
j = k-1
# print(j)
min = float('inf')
        
while j < len(nums):

    if nums[j] - nums[i] < min:
        min = nums[j] - nums[i]
            
    i+=1
    j+=1

print(min)


        