class Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.data = value
    
def Insert(root, value):
    if (root is None):
        return Node(value)
    if (root.data == value):
        return root
    if (root.data > value):
        root.left = Insert(root.left, value)
    else:
        root.right = Insert(root.right, value)
    return root
    
def get_successor(root):
  root = root.right
  while(root is not None and root.left is not None):
    root = root.left
  return root
  
def delete(root, value):    
  if(root is None):
    return root
  if(root.data > value):
    root.left = delete(root.left, value)
  elif(root.data < value):
    root.right = delete(root.right, value)
  else:
    if(root.left is None):
      return root.right
    if(root.right is None):
      return root.left
    else:
      successor = get_successor(root)
      root.data = successor.data
      root.right = delete(root.right, successor.data)
  return root
  
def inOrder(root):
  if (root is not None):
    inOrder(root.left)
    print(root.data, end=" ")
    inOrder(root.right)


root = Insert(None, 20)
root = Insert(root, 15)
root = Insert(root, 30)
root = Insert(root, 40)
root = Insert(root, 12)
root = Insert(root, 18)
root = Insert(root, 25)
root = Insert(root, 50)

inOrder(root) 

delete(root, 30)
print("\nAfter deleting 12: ")
inOrder(root)