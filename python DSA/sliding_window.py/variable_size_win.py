#my approch for max sum

'''arr =[4,1,1,1,1,3,5]
k = 5 #sum of elemnts = 5

i,j,sum,large =0,0,0,0

while j<len(arr):
    sum +=arr[j]
    while sum>k:
        sum -= arr[i]
        i += 1
    if sum<k:
        j +=1
    elif sum ==k:
        if large < j-i+1:
            large = j-i+1
        sum -= arr[i]
        i+=1
        j+=1
print(large)
'''

#chatgpt approach for max sum ...write it down in your copy
'''
arr = [4, 1, 1, 1, 1, 3, 5]
k = 5  # target sum
i, j, current_sum, max_length = 0, 0, 0, 0

while j < len(arr):
    current_sum += arr[j]
    
    # Adjust the left pointer if the sum exceeds k
    while current_sum > k and i <= j:
        current_sum -= arr[i]
        i += 1
    
    # Check for the condition when the current sum equals k
    if current_sum == k:
        max_length = max(max_length, j - i + 1)
    
    # Move to the next element
    j += 1

print(max_length)'''

#Leetcode question...without repeating characters
#MY approach failed! :(
'''s = "tmmzuxt"

i,j,large,repeat = 0,0,0,False
dict ={}

while j<(len(s)):
    if s[j] in dict:
        dict[s[j]] +=1
        repeat = True
       
    else:
        dict[s[j]] =1
        
    if repeat == False:
        j +=1
        if j-i > large:
            large = j-i
            
       
    elif repeat == True:
        if large <  j-i:
            large = j-i

        dict[s[i]] -=1
        
        if s[j] == s[i]:
            j+= 1
       
        i +=1
        repeat = False
        
if large ==0 and dict:
    large = 1
print(large)
'''
#CHATGPT approach 
'''

s = ""

i, j, large = 0, 0, 0
char_count = {}

while j < len(s):
    if s[j] in char_count and char_count[s[j]] > 0:
        # Character is a repeat, so move the left pointer
        char_count[s[i]] -= 1
        i += 1
    else:
        # No repeat, add to the count and move the right pointer
        char_count[s[j]] = char_count.get(s[j], 0) + 1
        large = max(large, j - i + 1)
        j += 1

print(large)'''

#Longest substring without repeating characters
s = "tmmzuxt"
count ={}
sz,repeat,i,j = 0,0,0,0
while j<len(s):
    if s[j] in count:
        count[s[j]]+=1
        repeat +=1
    else:
        count[s[j]] =1
    while repeat>0:
        count[s[i]] -=1
        if count[s[i]]==1:
            repeat -=1
        elif count[s[i]]==0:
            del count[s[i]]
        i+=1
    if repeat ==0:
        sz = max(sz, len(count))
    j+=1
print(sz)



