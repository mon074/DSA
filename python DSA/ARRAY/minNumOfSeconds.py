mountainHeight = 5
workerTimes = [1]

workerTimes.sort()

mxsum = float("-inf")
mh = mountainHeight
n = len(workerTimes)
sum = 0

for i in workerTimes:

    h = -(-mh//n)

    for j in range(1,h+1):
        sum += i*j
    
    if sum> mxsum:
        mxsum = sum

    sum=0
    mh -=h
    n-=1
print(mxsum)