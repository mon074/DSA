s = "tmmzuxt"
count ={}
for j in s:
    if j in count:
        count[j]+=1
    else:
        count[j] =1
print(count)