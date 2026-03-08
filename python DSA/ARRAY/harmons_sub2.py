nums=[1,1,2,3,4]
d={}
for i in nums:
            d[i] = d.get(i, 0) + 1
    
print(d)