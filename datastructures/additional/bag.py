'''
Bag:which stores the items in duplicates and the count of items
'''
class Bag():
    def __init__(self):
        self.bag = {}
    def add(self, item):
        self.bag[item] = self.bag.get(item,0)+1
    def remove(self, item):
        if item in self.bag:
            if self.bag[item] > 1:
                self.bag[item] -= 1
            else:
                del self.bag[item]
    def count(self, item):
        return self.bag.get(item, -1)
bag=Bag()
bag.add('apple')
bag.add('apple')
bag.add('apple')
bag.add('banana')
print(bag.count('apple'))
