class CircularQueue:
  def __init__(self, size):
    self.size = size
    self.items = [None] * size
    self.front = self.rear = -1
    
  def enqueue(self, value):  # Insert Method
    if((self.rear + 1) % self.front):
      print("Queue is Full")
    elif(self.front == -1):
      self.front = self.rear = 0
      self.items[self.rear] = value
    