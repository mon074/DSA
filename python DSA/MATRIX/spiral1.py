matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
j=0
i=-1
r=0
t =0
ans=[]

while t<len(matrix)*len(matrix[0]):

    if t<len(matrix)*len(matrix[0]): 
        for i in range(i+1,len(matrix[0])-r):
            ans.append(matrix[j][i])
            t+=1
    if t<len(matrix)*len(matrix[0]):    
        for j in range(j+1, len(matrix)-r):
            ans.append(matrix[j][i])
            t+=1
    if t<len(matrix)*len(matrix[0]):
        for i in range(i-1,-1+r,-1):
            ans.append(matrix[j][i])
            t+=1
        else:
            r+=1
    if t<len(matrix)*len(matrix[0]):    
        for j in range(j-1,-1+r,-1):
            ans.append(matrix[j][i])
            t+=1

print(ans)