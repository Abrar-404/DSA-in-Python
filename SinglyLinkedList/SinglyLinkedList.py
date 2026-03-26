class Node:
  def __init__(self, info, next=None):
    self.info = info
    self.next = next


class SinglyLinkedList:
  def __init__(self, head=None):
    self.head = head

  def insertAtEnd(self, value):
    temp = Node(value)
    if(self.head != None):
      t1 = self.head

      while(t1.next != None):
         t1 = t1.next
      t1.next = temp

    else:
      self.head = temp

  def PrintLL(self):
    t1 = self.head
    while(t1.next != None):
      print(t1.info)
      t1 = t1.next

    print(t1.info)


obj = SinglyLinkedList()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.PrintLL()