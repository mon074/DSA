nums = [10,2]

#using insertion sort here
nums[0]=str(nums[0])
for i in range (1,len(nums)):
    key = str(nums[i])
    j=i-1

    while j>=0 and key+str(nums[j])>str(nums[j])+key:
        nums[j+1]=nums[j]
        j-=1
    nums[j+1]=key

print(''.join(nums))