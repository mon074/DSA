nums = [2,3,4,1,2]
# nums =[2,5,9,6,9,3,8,9,7,1]


for j in range(1,len(nums)):
    # count=0
    m,n=0,j
    while n<len(nums):

        if nums[m]==nums[n]:
            print(nums[m])
            break
        m+=1
        n=m+j
        