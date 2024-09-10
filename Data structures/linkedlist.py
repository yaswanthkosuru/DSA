'''
linked list :stores [1,address]->[2,address]->[3,address]
and so on ...
'''

def tests():
    l=[1,2,3,4,5,6,7,8,9,10,11]
    ll=LinkedList()
    for i in l:
        ll.insert_at_end(i)
    ll.remove_at_beginning()
    ll.remove(11)
    ll.print()

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList():
    def __init__(self) -> None:
        self.head = None
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    def remove_at_beginning(self):
        if self.head is None:
            return
        data=self.head.data
        self.head=self.head.next
        return data
    def remove(self,data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current_node = self.head
        while current_node.next and current_node.next.data != data:
            current_node = current_node.next
        if current_node.next:
            current_node.next = current_node.next.next
    def print(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' ')
            current_node = current_node.next
        print()
