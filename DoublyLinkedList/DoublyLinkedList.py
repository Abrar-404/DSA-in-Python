class Node:
  def __init__(self, value=None):
    self.info = value
    self.prev = None
    self.next = None
    
    
class DoublyLinkedList:
  def __init__(self):
    self.head = None
    
    
  def insertAtBeg(self, value):
    temp = Node(value)
    if(self.head == None):  # noqa: E711
      self.head = temp
      return
    temp.next = self.head
    self.head.prev = temp
    self.head = temp
    
    
  def insertAtMid(self, value, x):
    t = self.head
    
    # searching method
    while(t.next != None):  # noqa: E711
      if(t.info == x):
        break
      else:
        t = t.next
    # searching method
        
    temp = Node(value)
    temp.next = t.next
    temp.prev = t
    t.next = temp
    temp.prev = t
    
  def insertAtEnd(self, value):
    temp = Node(value)
    if(self.head == None):  # noqa: E711
      self.head = temp
      return
    
    t = self.head
    while(t.next != None):  # noqa: E711
      t = t.next
      
    t.next = temp
    temp.prev = t
    
  def deleteDLL(self, value):
    if(self.head == None):  # noqa: E711
      print("Linked List is empty")
      return
    
    t = self.head
    if(t.info == value):
      self.head = t.next
      self.head.prev = None
      return
    
    while(t.next != None):  # noqa: E711
      if(t.info == value):
        t.prev.next = t.next
        t.next.prev = t.prev
        return
      else:
        t = t.next
    
    if(t.info == value):
      t.prev.next = None
      return
    
  def printDLL(self):
    t = self.head
    while(t.next != None):  # noqa: E711
      print(t.info)
      t = t.next
    print(t.info)
    
    

obj = DoublyLinkedList()
obj.insertAtBeg(5)
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtMid(25, 20)
obj.insertAtEnd(30)
obj.insertAtEnd(40)
obj.deleteDLL(40)
obj.printDLL()
