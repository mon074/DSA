#pattern11..khud kia mene :D also write down both of them 
#my approach
'''from collections import deque
Q = deque()
Q.append(1)
Q.append(0)
for i in range(1,6):
    for j in range(i):
        m=Q.popleft()
        print(m,end=" ")
        Q.append(m)
    print()'''
#striver's approach 
#note:- to flip 0 and 1 use num = 1-num..it will flip 0 to 1 and vice versa highlight this!
'''n=5
for i in range(n):
    if i%2==0:
        start =1
    else:
            start = 0
    for j in range(i+1):
         print(start,end=" ")
         start = 1-start #Flip
         print()'''
#pattern12..i did it :D
#My approach dont write in copy
'''n=4
m= n*2-2
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    for j in range(n*2-2*i):
        print(" ",end=" ")
    for j in range(i):
        print(i-j,end=" ")
    print()'''
#striver's approach...write in copy
'''n=4

space = 2*(n-1)
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    for j in range(space):
        print(" ",end=" ")
    for j in range(i,0,-1):
        print(j,end=' ')
    print()
    space -=2'''
#theory of reversed for loop write in copy!
'''N = 6

# without using reversed() to perform the back iteration 
print ("The reversed numbers are : ", end = "") 
for num in range(N, -1, -1) : 
    print(num, end = " ") 
output->>> The reversed numbers are : 6 5 4 3 2 1 0 '''

#pattern13 don't write in copy
#my approach and striver's same 
'''num =1
for i in range(5):
    for j in range(i+1):
        print(num,end=" ")
        num+=1
    print()'''
#pattern14 
#my approach
'''char =['A','B',"C",'D','E']
for i in range(5):
    for j in range(i+1):
        print(char[j], end=" ")
    print()'''
#striver's approach write down in copy
'''for i in range(5):
    ch = (ord('A') + i) # Calculate the ASCII corresponding to 'A' + i
    for j in range(ord('A'), ch + 1):  # Loop from 'A' to the character `ch`
        print(chr(j), end=' ')  # Convert the ASCII value back to a character for printing
    print()'''  # Print a newline after each row
'''#note->>>Explanation:
chr() converts an ASCII code to a character.
ord() converts a character to its ASCII code.'''
#pattern15
#my approach same approach
'''n=5
lim = ord('A')+5
for i in range(5):
    for j in range(ord('A'),lim-i):
        print(chr(j),end=' ')
    print()'''