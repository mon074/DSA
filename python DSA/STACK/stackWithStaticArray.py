#Stack Implementation using an array 
# it is a static stack cause capacity is fixed
class myStack:

    def __init__(self,cap):

        self.arr = [0]*cap
        self.capacity = cap
        self.top = -1

stack1 = myStack(3)

#Push operation my code time:O(1) and space:O(1)
# here carefullly increment the top only after checking the condition or 
# it give wrong answers during pop 
# if top's value is wrong
def push(self,data):

    
    
    if self.top +1 < self.capacity:
        self.top +=1
        self.arr[self.top] = data
        return True
    
    else:
        print("Stack Overflow!!!")
        return False

#Gfg code Follow this! time:O(1) and space:O(1)
def push(self, x):
    
    if self.top == self.capacity - 1:
        print("Stack Overflow")
        return
    
    self.top += 1
    
    self.arr[self.top] = x

push(stack1,10)
push(stack1,20)
push(stack1,30)
# push(stack1,40)


#Time: O(1) and space:O(1)
def pop(self):
    
    if self.top == -1:
        print("Stack Underflow")
        return -1
    
    value = self.arr[self.top]
    self.top -= 1
 
    return value

#peek or top return the element on top
#time: O(1) and Space:(1)
def peek(self):
  
    if self.top == -1:
        print("Stack is Empty")
        return -1
  
    return self.arr[self.top]

print(peek(stack1))

# Returns true if the stack is empty, else false.
#time:O(1) and space:O(1)
def isEmpty(self):
   
    return self.top == -1

print(isEmpty(stack1))

# Returns true if the stack is full, else false.
#time:O(1) and space:O(1)

def isFull(self):

    return  self.top == self.capacity-1

print(isFull(stack1))