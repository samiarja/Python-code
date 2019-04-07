#Searching for key
###########################################################3
def search(root, key):
    #if root is null of the key is present in root, than return root value
    if root is None or root.val == key:
        return root

    #if key is greater than root
    if key.val > root:
        return search(root.rigt, key)

    #if key is less than root
    if key.val < root:
        return search(root.left, key)

print("BST Search is done!!")

#Insertion of a key in BST
###########################################################3
# A new value is always inserted a leaf

class Node:
    #A class that represent an individual node in BST
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
#A function that insert a new node with the given key
def insert(root,node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)
#A function to perform the inorder tree traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
r = Node(50)
insert(r,Node(30)) 
insert(r,Node(20)) 
insert(r,Node(40)) 
insert(r,Node(70)) 
insert(r,Node(60)) 
insert(r,Node(80))

inorder(r)













    
                
    
