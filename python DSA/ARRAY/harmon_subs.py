nums = [1,3,2,2,5,2,3,7]

d = {nums[0]:[0,1],}
max=0
for i in range(1,len(nums)):

    for key in d:
        if key-nums[i]==1:
            d[key][0]+=1
            if (d[key][0]+d[key][1])>max:
                max= d[key][0]+d[key][1]

        elif nums[i]==d[key]:
                d[key][1]+=1
                if d[key][0]>0 and (d[key][0]+d[key][1])>max:
                    max=d[key][0]+d[key][1]
            
        else:
            d[nums[i]]=[0,1]
            break
print(max)

print(d)