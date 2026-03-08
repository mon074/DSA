nums = [1,3,4,2,2]

sum=0

for i in range(1,len(nums)):
    sum+=i


for i in nums:
    sum-=i

print(int(str(sum)[1]))