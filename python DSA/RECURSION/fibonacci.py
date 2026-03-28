n=10


temp=0
# flag=n

def fib(x,flag):
    global n
    global temp
      
    sum = temp+x
    temp = x

    if n<=0:
        return "invalid position"
    if n==1:
        return 0
    elif n==2:
        return 1
    
    if flag==2:

        return x
    
    return fib(sum,flag-1)

print(fib(1,n))

    