class Stack:
  def __init__(self):
    self.stackList = []
    
  def length(self):
    return len(self.stackList)
  
  def push(self, value):
    self.stackList.insert(0, value)
    
  def peek(self):
    if len(self.stackList) == 0:
      raise Exception("Stack is empty")
    else:
      return self.stackList[0]
    
  def pop(self):
    if len(self.stackList) == 0:
      raise Exception("Stack is empty")
    else:
      return self.stackList.pop(0)
    

stackObj = Stack()

stackObj.push(10)
stackObj.push(20)
stackObj.push(30)
stackObj.push(40)

print(stackObj.peek())

print(stackObj.pop())
print(stackObj.pop())
print(stackObj.pop())
print(stackObj.pop())