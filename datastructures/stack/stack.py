'''
first in last out
like tower of hanoi person comes first get out last.
'''
class Stack():
    def __init__(self) -> None:
        self.stack=[]
    def insert(self,item):
        self.stack.append(item)
    def pop(self):
        if (self.is_empty()):
            return -1
        return self.stack.pop()
    def peek(self):
        if (self.is_empty()):
            return -1
        return self.stack[-1]
    def is_empty(self):
        return len(self.stack) == 0
stack=Stack()
stack.insert(0)
stack.insert(1)
stack.insert(2)
print(stack.peek())
print(stack.pop())
print(stack.peek())