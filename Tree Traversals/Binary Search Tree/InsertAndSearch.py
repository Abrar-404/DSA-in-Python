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

def Search(root, value):
    if (root is None):
        print('Element not found in the tree', end="\n")
        return
    if (root.data == value):
        print('Element found in the tree', end="\n")
        return
    if (root.data > value):
        Search(root.left, value)
    else:
        Search(root.right, value)
    return root

def inOrder(root):
    if root is not None:
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
Search(root, 18)