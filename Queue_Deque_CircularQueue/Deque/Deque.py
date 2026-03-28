class Deque:
  def __init__(self):
    self.items = []
    
  def isEmpty(self):
    return len(self.items) == 0
  
  def insertAtFront(self, value):
    self.items.insert(0, value)
  
  def insertAtEnd(self, value):
    self.items.append(value)
    
  def deleteAtFront(self):
    if(self.isEmpty()):
      print("Deque is empty")
      # raise Exception("Deque is empty") # For Python 3 ==> it is an another way to handle the error instead of print statement
    else:
      return self.items.pop(0)
    
  def deleteAtEnd(self):
    if(self.isEmpty()):
      print("Deque is empty")
      # raise Exception("Deque is empty") # For Python 3 ==> it is an another way to handle the error instead of print statement
    else:
      return self.items.pop()
    

dq = Deque()

dq.insertAtFront(20)
dq.insertAtEnd(10)
dq.insertAtFront(40)
dq.insertAtEnd(30)

print(f"Deque before delete: {dq.items}")
print(dq.deleteAtEnd())
print(dq.deleteAtFront())
print(dq.deleteAtEnd())
print(dq.deleteAtFront())

dq.deleteAtFront() # it will print "Deque is empty" because there is no element in the deque
dq.deleteAtEnd() # it will print "Deque is empty" because there is no element in the deque
print(f"Deque after delete: {dq.items}")