matrix = [[3,7,8],[9,11,13],[15,16,17]]
matrix = [[7,8],[1,2]]
matrix = [[3,6],[7,1],[5,2],[4,8]]
lucky = []
# p=[]
r=0
temp=r+1

while r<len(matrix):
    m=float('inf')
    for c in range(len(matrix[0])):
        if matrix[r][c]<m:
            m = matrix[r][c]
            pos = c
    temp=0
    while temp<len(matrix):
        if matrix[temp][pos]>m:
            r+=1
            break
        else:
            temp+=1
    else:
        # if pos not in p:
            lucky.append(m)
            # p.append(pos)
            r+=1
        # else:
            # r+=1
            # break

print(lucky)
        