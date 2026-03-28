class Queue:
  def __init__(self):
    self.items = []
    
  def isEmpty(self):
    return len(self.items) == 0
  
  def insert(self, value):
    self.items.append(value)
    
  def delete(self):
    if (self.isEmpty()):
      print("Queue is empty")
      # raise Exception("Queue is empty") # For Python 3 ==> it is an another way to handle the error instead of print statement
    else:
      return self.items.pop(0)
    

q = Queue()

q.insert(10)
q.insert(20)
q.insert(30)
q.insert(40)
q.insert(50)

print(f"Queue before delete: {q.items}")
print(q.delete())
print(q.delete())
print(q.delete())
print(q.delete())
print(q.delete())
q.delete()
print(f"Queue after delete: {q.items}")