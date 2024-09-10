'''
Que:first in first out .
like wating list before airport checking.
'''

'''
using list
'''

def tests():
    queue=Que_LL()
    queue.enqueue(0)
    queue.enqueue(1)
    print(queue.dequeue())

class Que():
    def __init__(self) -> None:
        self.queue=[]
    def enqueue(self,item):
        self.queue.append(item)
    def dequeue(self):
        if (self.is_empty()):
            return -1
        return self.queue.pop(0)
    def peek(self):
        if (self.is_empty()):
            return -1
        return self.queue[0]
    def is_empty(self):
        return len(self.queue) == 0
    def size(self):
        return len(self.queue)



# Using deque from collections module
from collections import deque

#using linked list
from linkedlist import LinkedList

class Que_LL():
    def __init__(self) -> None:
        self.queue=LinkedList()
    def enqueue(self,item):
        self.queue.insert_at_end(item)
    def dequeue(self):
        return self.queue.remove_at_beginning()

tests()



