#pattern6....i did it
'''n=5
for i in range(n):
    t =n-i
    for j in range(1,t+1):
        print(j,end=' ')
    print()'''
#pattern7 write in copy imp ...attempted
# break the inner loop into three parts(loops) one for space second for star third for space again
#observe the pattern of the space and star like :
# i=0, [4,1,4]
#i=1, [3,3,3]
#i=3, [2,5,2]...here for space (n-i-1) and for star(2*i+1)
'''n=5
for i in range(n):
    for j in range(n-i-1):
        print(" ",end = " ")
    for j in range(2*i+1):
        print("*",end = " ")
    for j in range(n-i-1):
        print(" ",end = " ")
    print()'''

#pattern8 write in copy..i did it
#formula for star= m-2*i where m = 9 = n*2-1 and for space = i..0,1,2.. so on.
'''n=5
m= n*2-1
for i in range(5):
    for j in range(i):
        print(" ",end=" ")
    for j in range(m-2*i):
        print("*",end=" ")
    for j in range(i):
        print(" ", end=" ")
    print()'''
#pattern9 ..i solved it
'''n=5
for i in range(n):
    for j in range(n-i-1):
        print(" ",end = " ")
    for j in range(2*i+1):
        print("*",end = " ")
    for j in range(n-i-1):
        print(" ",end = " ")
    print()
m= n*2-1
for i in range(5):
    for j in range(i):
        print(" ",end=" ")
    for j in range(m-2*i):
        print("*",end=" ")
    for j in range(i):
        print(" ", end=" ")
    print()
'''
#pattern10
#my logic
'''n=5
m = n-1
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(m):
    for j in range(m-i):
        print("*", end=" ")
    print()'''
#striver's approach
'''n=5
for i in range(1,2*n):
    stars= i
    if i>n:
        stars = 2*n-i #2*5-6 = 4
    for j in range(stars):
        print("*",end =" ")
    print()'''
