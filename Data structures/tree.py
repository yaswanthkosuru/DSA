'''
left child and right child relation starting from root
     2
    / \
   3   4
  / \ / \
 3  5 6  7


notes:different types of trees
'''

def tests():
    #create a tree instance
    tree = Tree(4)
    #add left child
    tree.root.left = Node(3)
    #add right child
    tree.root.right = Node(5)
    print(tree.root.left.data)
class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree():
    def __init__(self,data):
        self.root = Node(data)
tests()