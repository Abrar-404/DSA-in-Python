class Node:
  def __init__(self, info, next=None):
    self.info = info
    self.next = next


class SinglyLinkedList:
  def __init__(self, head=None):
    self.head = head


  def insertAtBeg(self, value):
    temp = Node(value)
    temp.next = self.head
    self.head = temp

  def insertAtMid(self, value, x):
    temp = Node(value)
    t1 = self.head

    while(t1.next != None):
      if(t1.info == x):
        temp.next = t1.next
        t1.next = temp
      t1 = t1.next

  def deleteLL(self, value):
    t1 = self.head
    prev = t1

    if(t1.info == value):
      self.head = t1.next

    while(t1.next != None):
      if(t1.info == value):
        prev.next = t1.next
        break
      else:
        prev = t1
        t1 = t1.next

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
obj.insertAtBeg(5)
obj.insertAtMid(40, 20)
obj.deleteLL(5)
obj.PrintLL()