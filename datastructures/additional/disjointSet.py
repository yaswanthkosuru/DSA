'''
helps in maintaing Disjoint sets
parent child relationship 
Algorithm:

store parent and connect small one below by size .while traversing do path compression 
roughly it takes o(logn) for union and connectivity test.
'''

def tests():
    ds=DisjointSet(8)
    ds.union(1,2)
    ds.union(2,3)
    ds.union(4,5)
    print(ds.connected(1,2))  # True
    print(ds.connected(2,3))  # False
    print(ds.connected(5,6))  # False
    ds.union(7,6)
    ds.union(5,7)
    ds.union(1,5)
    print(ds.connected(1,6))  # True
    print(ds.connected(1,5))  # True
class DisjointSet:
    def __init__(self, n):
        self.parent = {i: i for i in range(n)}
        self.size = [1] * n
    def findroot(self,x):
        while self.parent[x]!=x:
            self.parent[x]=self.parent[self.parent[x]]  # path compression technique to reduce height of the tree
            x=self.parent[x]
        return x
    def union(self, x, y):
        root_x = self.findroot(x)
        root_y = self.findroot(y)
        if root_x!=root_y:#smaller one goes below for small height
            if self.size[root_x]<self.size[root_y]:
                root_x, root_y = root_y, root_x
            self.parent[root_y] = root_x
            self.size[root_x]+=self.size[root_y]

    def connected(self, x, y):
        return self.findroot(x)==self.findroot(y)
    
tests()