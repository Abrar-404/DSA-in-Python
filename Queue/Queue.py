class Queue:
  def __init__(self):
    self.items = []
    
  def isEmpty(self):
    return len(self.items) == 0
  
  def insert(self, value):
    self.items.append(value)
    
  def delete(self):
    if (self.isEmpty()):
      raise Exception("Queue is empty")
    else:
      return self.items.pop(0)