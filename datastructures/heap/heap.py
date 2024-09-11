'''
heap:heap is complete binary tree we can pop element in o(1) and push element in o(1)
uses array to represent
maxheap:root is always max
minheap:root is always min
adjust from down,adjust from up,maintaining complete binary tree is important
internally use array to represent so it helps for upward traversal and lower traversal.
  1
 /  \
2    3
'''

#build min heap
class Heap:
    def __init__(self,heap):
        self.heap = heap
        self.heapsize=len(heap)
    
    def heappush(self,val):
        self.heap.append(val)
        self.heapsize+=1
        self._heapify_up(self.heapsize-1)
    

    def heappop(self):
        if self.heapsize == 0:
            raise IndexError("Heap is empty")
        root = self.heap[0]
        self.heap[0] = self.heap[self.heapsize - 1]
        self.heapsize -= 1
        self._heapify(0, self.heapsize)
        return root

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)


    def _heapify(self,index,heapsize):
        left=2*index+1
        right=2*index+2
        mini=index
        if left<heapsize and self.heap[left]<self.heap[mini]:
            mini=left
        if right<heapsize and self.heap[right]<self.heap[mini]:
            mini=right
        if mini!=index:
            self.heap[index],self.heap[mini]=self.heap[mini],self.heap[index]
            self._heapify(mini,heapsize)
    
    
    def heapify(self):
        arr=self.heap
        for i in range(len(arr)//2,-1,-1):
            self._heapify(i,self.heapsize)


a=[4,2,10,9,-1,-4,-3]
heap=Heap(a)

heap.heapify()

heap.heappush(8)
heap.heappop()
while heap.heapsize:
    print(heap.heappop())