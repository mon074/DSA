nums = [0,1,0,3,12]

z = 0
n=0
while n<len(nums):
    if nums[z]==0 and nums[n]!=0:
        if z<n:
            nums[z],nums[n] = nums[n],nums[z]
        else:
            n=z+1
    if nums[z] !=0:
        z+=1
    if nums[n] ==0:
        n+=1
    
print(nums, "...final")