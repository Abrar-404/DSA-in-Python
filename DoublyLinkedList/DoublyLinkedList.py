class Node:
  def __init__(self, value=None):
    self.info = value
    self.prev = None
    self.next = None
    
    
class DoublyLinkedList:
  def __init__(self):
    self.head = None
    
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
    
    
  def printDLL(self):
    t = self.head
    while(t.next != None):  # noqa: E711
      print(t.info)
      t = t.next
    print(t.info)
    
    

obj = DoublyLinkedList()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtEnd(40)
obj.printDLL()