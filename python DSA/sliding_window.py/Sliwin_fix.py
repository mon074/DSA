#max sum subarray of size 3
'''arr =[2,5,1,8,2,9,1] #19
wins = 3 #window size
size = len(arr)-1

i,j,sum,mx=0,0,0,0
while j<=size:
    sum = sum+arr[j]
    if j-i+1<wins:
        j+=1
    elif j-i+1==wins:
        mx = max(mx,sum)
        sum-=arr[i]
        j+=1
        i+=1
print("max sum of subarray",mx)'''

#first -ve number in every window of size wins..;)
arr = [12,-1,-7,8,-15,30,16,28]
wins = 3
i,j=0,0
neg = []
while j<len(arr):
    if arr[j]<0:
        neg.append(arr[j])
    if j-i+1<wins:
        j+=1
    elif j-i+1==wins:
        if not neg:
            print(0)
        else:
            print(neg[0])
            if arr[i]==neg[0]:
               neg.pop(0)
        j+=1
        i+=1
