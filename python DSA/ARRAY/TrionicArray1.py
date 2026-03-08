nums = [1,3,5,4,2,6]
nums=[2,1,3]
n= len(nums)
p,q,r=0,0,0

for i in range(n):

    if i<n-1:
        if nums[i]>nums[i+1]:
            if i>0:
                p=i
                break
            else:
                print(False)
    else:
        break
        print(False)

for j in range(p,n):
    if j<n-1:

        if nums[j]<nums[j+1]:
            if j>p:
                q=j
                break
            else:
                print(False)
                break
    else:
        print(False)
        break


for k in range(q,n):

    if k<n-1:
        if nums[k]>nums[k+1]:
            
            print(False)
            break
print(True)
