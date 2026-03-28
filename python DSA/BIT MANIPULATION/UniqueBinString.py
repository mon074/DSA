nums = ["111","011","001"]
n = len(nums)

# mx = int('1'*n,2)
# present = []

# for i in nums:
    
#     present.append(int(i,2))


# for j in range(0,mx+1):

#     if j in present:
#         continue
#     else:
#         x = bin(j)
#         ans = x[2:].zfill(n)
#         print(ans)


# print(present)



# print(mx)

#USing cantor's algorithm

ans = ''

for i in range(n):

    if nums[i][i] == '0':
        ans+='1'
    
    else:
        ans+='0'

print(ans)
