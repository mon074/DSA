s = "bbbbb"
i = 0
j = i+1
result = 0
size = 0 
while j<len(s):
    if s[i] != s[j]:
        j = j+1
    else:
        size = j-i
        while s[i]==s[j] and i<=j:
            i=i+1
    j=j+1
    result = max(result,size)
print(result)