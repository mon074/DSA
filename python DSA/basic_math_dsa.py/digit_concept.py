#(1).count the number of digits using digit concept
#note :- if you try to use len func then "TypeError: object of type 'int' has no len()"
'''n= 7789
count = 0
while n>0:
    n = n//10
    count +=1
print(count)'''
#using log base 10  and adding 1 to it to count digits
'''import math 
n = int(input("write a numbere here:"))
ans = int(math.log10(n)+1) #used int to convert the float value to int (actuallyt it was 4.9 something )
print(ans)'''
''' also remember if division of n is happening 10 time then time complexity is logbase10(n) if 
division is by 3 then time complexity is logbase3(n) therefor if the number of iterations
are based on division then the time complexity will depend upon log'''
#(2).reverse a number
#my approach
'''temp = ""
n = 10500
t = n%10
while t==0:
    n=n//10
    t = n%10
while n>0:
    temp=  temp + str(t)
    n = n//10
    t = n%10
print(int(temp))'''
#striver's approach
'''temp = 0
n = int(input('write a number to be reversed here:'))
while n>0:
    t = n%10
    temp = (temp*10)+t
    n = n//10
print(temp)'''
#(3). check whether number is palindrome or not!
#my approach == striver's approach
'''temp = 0
n = int(input('write a number to be reversed here:'))
check = n
while n>0:
    t = n%10
    temp = (temp*10)+t
    n = n//10
if temp==check:
    print("True")
else:
    print("False")'''
#(4). armstrong numbers
'''num =0
n = int(input("write a number here: "))
temp = n
while n>0:
    t = n%10
    num+= t**3
    n=n//10
if num == temp:
    print(True)
else:
    print(False)'''
#print all divisors
#normal approach
'''n = int(input("write a number :"))
for i in range(1,n+1):
    if n%i==0:
        print(i,"is a divisor")'''
#better approach
'''
import math
div =[]
n= int(input('write a number here: '))
for i in range(1,math.sqrt(n)):
    if n%i==0:
        div.append(i)
        if n%i!=i:
            div.apend(i)
print(div)
'''
PI = 3.1356
PI = 34
print(PI)
MI = "MONA"
print(type(MI))