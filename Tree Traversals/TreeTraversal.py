class Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.data = value
    
def preOrder(root):
  if(root != None):  # noqa: E711
    print(root.data, end = " ")
    preOrder(root.left)
    preOrder(root.right) 
    
def inOrder(root):
  if(root != None):  # noqa: E711
    inOrder(root.left)
    print(root.data, end = " ")
    inOrder(root.right)
  
def postOrder(root):
  if(root != None):  # noqa: E711
    postOrder(root.left)
    postOrder(root.right)
    print(root.data, end = " ")
    
root = Node(1)
root.left = Node(3)
root.right = Node(5)


root.left.left = Node(2)
root.left.right = Node(4)

root.right.right = Node(8)

preOrder(root)
inOrder(root)
postOrder(root)