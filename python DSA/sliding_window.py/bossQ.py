'''two strings are given to you find tehe min size substring in s (string) that 
contains all the characters of t (another string) quantity of those characters can increase 
but can't decrease'''

'''s= "timetopractise"
t="ttoc"

char={}
for c in t:
    if c in char:
        char[c] +=1
    else:
        char[c] =1
j,i,sz=0,0,float('inf')
count = len(t)
while j<len(s):
    if s[j] in char:
        char[s[j]] -=1
        if char[s[j]] ==0:
           count -=1
    while count==0:
        sz= min(j-i+1,sz)
        if s[i] in char:
            char[s[i]] +=1
            if char[s[i]] ==1:
               count +=1
        i+=1
    j+=1
print(sz)
'''

s = "timetopractise"
t = "toc"

char = {}
# Step 1: Store frequency of characters in t
for c in t:
    if c in char:
        char[c] += 1
    else:
        char[c] = 1

j, i, sz = 0, 0, float('inf')
count = len(char)  # To track how many characters of t we need in s
current_count = {c: 0 for c in char}  # To track current window frequency

# Step 2: Start sliding window
while j < len(s):
    if s[j] in char:  # Only process if the character is in t
        current_count[s[j]] += 1
        if current_count[s[j]] == char[s[j]]:
            count -= 1
    
    # Step 3: Shrink window when all characters are found
    while count == 0:
        sz = min(sz, j - i + 1)
        
        # Now try to shrink the window from the left
        if s[i] in char:
            current_count[s[i]] -= 1
            if current_count[s[i]] < char[s[i]]:
                count += 1
        
        i += 1  # Move left pointer to shrink window

    j += 1  # Move right pointer to expand window

# If sz is still inf, no valid window was found
if sz == float('inf'):
    print("No valid window found :(")
else:
    print(sz)
#congrats on completing sliding window ..keep it up* :D