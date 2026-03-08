#approch one (mine) is a naive method have o(n.n) complexity
arr = [1,3,-1,-3,5,3,6,7]
wsize = 3
i,j = 0,0
'''ans,temp = [],[]
#part 1
while j<len(arr):
    temp.append(arr[j])
    if j-i+1<wsize:
        j += 1
    elif j-i+1 == wsize:
        maxi = max(temp)
        ans.append(maxi)
        temp.remove(arr[i])
        i +=1
        j += 1
print(ans)'''
# SUCCESS!

#approach 2 of youtube
#optimized approach
ans =[]
from collections import deque
q = deque()
while j<len(arr):
    while q:
        if q[0] <= arr[j]:
            q.popleft()
        else:
            break
    q.append(arr[j])
    if j-i+1 < wsize:
        j +=1
    elif j-i+1 == wsize:
        ans.append(q[0])
        if q[0] == arr[i]:
            q.popleft()
        i+=1
        j+=1
print(ans)
#success2

