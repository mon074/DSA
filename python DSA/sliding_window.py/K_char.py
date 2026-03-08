#gpt ka solution not mine :(
#k unique character

s= "aabacbebebe"
k =3
count = {}
unique,i,j =0,0,0
long = 0
while j<len(s):
    if s[j] in count:
        count[s[j]] +=1
    else:
        count[s[j]] =1
        unique +=1
    while unique >k:
        if s[i] in count:
            count[s[i]] -=1
        if count[s[i]] ==0:
            unique -=1
            del count[s[i]]
        i+=1
    if unique ==k:
        long =max(long,j-i+1)
    j+=1
print(long)

