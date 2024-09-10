'''
for every node left side elements are smaller than right side elements
properties:inorder is in sorted order.
'''
def tests():
    bst=Bst()
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)
    bst.delete(20)
    bst.delete(50)
    bst.delete(30)
    bst.delete(70)
    bst.inorder()


class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class Bst:
    def __init__(self):
        self.root = None

    def _inorder(self,root):
        if root:
            self._inorder(root.left)
            print(root.data, end=' ')
            self._inorder(root.right)
    def inorder(self):
        if not self.root:
            return
        self._inorder(self.root)
        print()
    
    def getsuccesor(self):
        if self.root is None:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current.data
    
    def findpredecessor(self,root):
        temp=root
        while temp.left and temp.left !=None:
            temp=temp.left
        return temp


    def insert(self,data):
        temp=self.root
        if temp==None:
            self.root=Node(data)
            return
        while temp!=None:
            if data<temp.data:
                if temp.left==None:
                    temp.left=Node(data)
                    break
                temp=temp.left
            else:
                if temp.right==None:
                    temp.right=Node(data)
                    break
                temp=temp.right
    def _delete_helper(self,root):
        if root is None:
            return root
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        right=root.right
        left=root.left
        lastleft=self.findpredecessor(right)
        lastleft.left=left
        return root.right

    def delete(self,val):
        temp=self.root
        if self.root.data==val:
            self.root=self._delete_helper(self.root)
            return

        while temp:
            if temp.left and temp.left.data==val:
                temp.left=self._delete_helper(temp.left)
                break
            if temp.right and temp.right.data==val:
                temp.right=self._delete_helper(temp.right)
                break
            if val<temp.data:
                temp=temp.left
            else:
                temp=temp.right

tests()