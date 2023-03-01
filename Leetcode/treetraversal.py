
class Node():
    def __init__(self,val=None) -> None:
        self.left = None
        self.right = None
        self.val = val

    def insert(self,val):
        if self.val:
            if val < self.val:
                if not self.left:
                    self.left = Node(val)
                else:
                    self.left.insert(val)
            else:
                if not self.right:
                    self.right = Node(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val

# creating a tree:
def createTree(arr):
    root = Node()
    for elem in arr:
        root.insert(elem)
    return root
arr = [1,2,3,4,5,6,7]
head = createTree(arr)

# Pre-order Traversal - Travel left node first:
def preOrdTravel(t1):
    print(t1.val, end=" ")

    if t1.left:
        preOrdTravel(t1.left)
    if t1.right:
        preOrdTravel(t1.right)
preOrdTravel(head)

# DFS - Post-Order Traversal - Go as deep as possible, then backtrack

def postOrderTravel()





