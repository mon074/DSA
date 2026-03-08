#pattern16
#My approach
'''char = ord("A")
for i in range(5):
    for j in range(i+1):
        print(chr(char),end=" ")
    char +=1
    print()'''
#striver's approach
'''char = ord("A")
for i in range(5):
    for j in range(i+1):
        print(chr(char+i),end=" ")
    print()'''
#pattern17
#my approach
'''char = ord("A")
space =3
for i in range(4):
    for j in range(space-i):
        print(" ",end=" ")
    for j in range(i+1):
        print(chr(char+j),end=" ")
    if i>=1:
        for j in range(i):
            print(chr(char+j),end=" ")
    for j in range(space-i):
        print(" ",end=" ")
    print()'''
#striver's approach write in copy ...

'''n=5
space =4
for i in range(n):
    for j in range(space-i):
        print(" ",end=" ")
    char =ord("A")
    breakpoint = (2*i+1)/2
    for j in range(1,2*i+2):
        print(chr(char),end=" ")
        if j<=breakpoint:
            char +=1
        else:
            char -=1
    for j in range(space-i):
        print(" ",end=" ")
    print()
'''
#pattern18
#My approach
'''char = ord('E')
n=5
for i in range(n):
    for j in range(i+1):
        c  = char+j
        print(chr(c),end=" ")
    char -=1
    print()'''
#striver's approach..note:- here see from where the loop is being started (observe the pattern)
#see where it is being ended (observe the pattern)
'''char = ord("E")
n= 5
for i in range(n):
    for j in range(char-i,char+1):
        print(chr(j),end=" ")
    print()'''
#pattern19
'''n=5
for i in range(5):
    for j in range(n-i):
        print("*",end=" ")
    for j in range(2*i):
        print(" ",end=" ")
    for j in range(n-i):
        print("*",end=" ")
    print()
space=2*n-2
for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    for j in range(space-2*i):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()'''

#pattern20
#my approach
'''n=5
space = 2*n-2
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    for j in range(space-2*i):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range(n-1):
    for j in range(n-i-1):
        print("*",end=" ")
    for j in range(2*i+2):
        print(" ",end=" ")
    for j in range(n-i-1):
        print("*",end=" ")
    print()'''
#striver's code
'''n=5
space = 2*n-2
for i in range(1,2*n):
    stars=i
    if i>n:
        stars= 2*n-i
    for j in range(stars):
        print("*",end=" ")
    for j in range(space):
        print(" ",end=" ")
    for j in range(stars):
        print("*",end=" ")
    print()
    if i<n:
        space -=2
    else:
        space+=2'''
#pattern21
#write in copy 
#striver's approach
'''n=4
for i in range(1,n+1):
    for j in range(n):
        if i==1 or j==0 or i==n or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''
#pattern22
#note:-
'''top= i,left= j, right= n-j-1,down= n-i-1'''
# Define the size of the matrix 
n = 7
a=4

# Loop through each row and column to fill the matrix
for i in range(n):
    for j in range(n):
        # Calculate the number to print based on the minimum distance to the edge
        num = min(i, j, n - i - 1, n - j - 1)
        num=a-num
        print(num, end=" ")
    print()  # Newline after each row






