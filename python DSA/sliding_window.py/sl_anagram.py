s ="cbaebabacd"
p = "abc"
count_d = {} #map
i,j=0,0
ans = []
for text in p:
    if text in count_d:
        count_d[text] += 1
    else:
        count_d[text] = 1
number = len(count_d)
while j<len(s):
    if s[j] in count_d:
        count_d[s[j]] -= 1
        if count_d[s[j]] == 0:
            number -= 1
    if j-i+1 <len(p):
        j+=1
    elif j-i+1 == len(p):
        if number == 0:
            ans.append(s[i])
        if s[i] in count_d:
            count_d[s[i]] +=1
            if count_d[s[i]]==1:
                number += 1
        i += 1
        j += 1
print(ans)


    
print(number)
print(count_d)