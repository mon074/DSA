#pattern1
'''for i in range(0,4):
    for j in range(0,4):
        print("*",end =' ')
    print(end ='\n')
'''
#pattern2...write in copy :D
'''# Outer loop for each row (1 to 4)
for i in range(1, 5):  # i starts at 1 and goes up to 4
    # Inner loop for printing stars
    for j in range(i):  # j loops from 0 to i-1 (printing i stars in each row)
        print("*", end="")  # print stars on the same line (end="" avoids newline)
    
    # After printing all stars for a row, move to the next line
    print() or you can write print(end="\n")  # This print statement moves to the next line
'''
#...pattern3...
#approach1
'''for i in range(1,6):
    for j in range(i):
        print(j+1,end=' ')
    print()'''
#approach2...write this one in copy
'''for i in range (1,6):
    for j in range(1,i+1):
        print(j,end=' ')
    print()'''

#pattern4 
'''for i in range(1,6):
    for j in range(i):
        print(i,end=' ')
    print()'''
#pattern5 write in copy
'''n=5
for i in range(5):
    t = n-i
    for j in range(t):
        print("*",end = " ")
    print()'''
