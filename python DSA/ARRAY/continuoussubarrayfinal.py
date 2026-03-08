nums =[5,0,0]
k=6

# sum=0
# s = set()
# for i in nums:
#     sum+=i
#     if sum%k==0:
#         print(True)
#         break
#     else:
#         if sum%k in s:
#             print(True)
#             break
#         else:
#             s.add(sum%k)
# else:
#     print(False)
# print(s)
# [0,1,0,3,0,4,0,4,0]

sum=0
s = {}
if len(nums)>1:
    for i in range(len(nums)):
        sum+=nums[i]
        if sum%k==0:
            print(True)
            break
        else:
            if sum%k in s and i>1 and s[sum%k]!=i-1:
                print(True)
                break
            else:
                if sum%k not in s:
                    s[sum%k]=i
    else:
        print(False)
else:
    print(False)
print(s)