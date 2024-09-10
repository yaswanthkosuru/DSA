# Types of Queues in DSA

A **queue** is a linear data structure that follows the **FIFO** (First In, First Out) principle. The element that is added first is the first one to be removed.

---

## 1. **Simple Queue**

A **Simple Queue** (also called a **Linear Queue**) is the most basic type of queue where elements are inserted at the rear and removed from the front.

### Structure

- **Front**: Points to the first element.
- **Rear**: Points to the last element.

### Operations

- **Enqueue**: Add an element to the rear of the queue.
- **Dequeue**: Remove an element from the front of the queue.
- **Peek/Front**: Access the front element without removing it.

---

## 2. **Circular Queue**

A **Circular Queue** is a type of queue where the last position is connected back to the first position to make a circular structure. It overcomes the limitation of the simple queue, where empty spaces may remain unused after `dequeue` operations.

### Structure

- **Front**: Points to the first element.
- **Rear**: Points to the last element.
- The rear is connected to the front when the end of the array is reached.

### Operations

- **Enqueue**: Insert an element at the rear in a circular manner.
- **Dequeue**: Remove an element from the front in a circular manner.
- **Peek/Front**: Access the front element without removing it.

---

## 3. **Priority Queue**

A **Priority Queue** is a type of queue where each element has a priority. The element with the highest priority is dequeued first, not necessarily the element that has been in the queue the longest.

### Structure

- Elements are ordered based on their priority.
  
### Operations

- **Enqueue**: Insert an element based on its priority.
- **Dequeue**: Remove the element with the highest priority.
- **Peek**: Access the element with the highest priority without removing it.

### Variants

- **Min Priority Queue**: The element with the lowest value has the highest priority.
- **Max Priority Queue**: The element with the highest value has the highest priority.

---

## 4. **Double-ended Queue (Deque)**

A **Deque (Double-ended Queue)** allows insertion and deletion at both ends. It can function as both a queue and a stack.

### Structure:

- **Front**: Points to the front element.
- **Rear**: Points to the rear element.

### Operations:

- **Enqueue Front**: Insert an element at the front.
- **Enqueue Rear**: Insert an element at the rear.
- **Dequeue Front**: Remove an element from the front.
- **Dequeue Rear**: Remove an element from the rear.

---

## 5. **Input-restricted Deque**

An **Input-restricted Deque** allows insertion only at one end (rear) but allows deletion from both ends (front and rear).

### Operations:

- **Enqueue**: Insert an element at the rear only.
- **Dequeue Front**: Remove an element from the front.
- **Dequeue Rear**: Remove an element from the rear.

---

## 6. **Output-restricted Deque**

An **Output-restricted Deque** allows deletion only from one end (front) but allows insertion from both ends (front and rear).

### Operations:

- **Enqueue Front**: Insert an element at the front.
- **Enqueue Rear**: Insert an element at the rear.
- **Dequeue**: Remove an element from the front only.

---

## 7. **Circular Deque**

A **Circular Deque** is a circular version of the double-ended queue where both the front and rear pointers are connected in a circular manner, allowing wrap-around when the end of the array is reached.

### Operations:

- **Enqueue Front**: Insert an element at the front in a circular manner.
- **Enqueue Rear**: Insert an element at the rear in a circular manner.
- **Dequeue Front**: Remove an element from the front in a circular manner.
- **Dequeue Rear**: Remove an element from the rear in a circular manner.

---

## 8. **Concurrent Queue**

A **Concurrent Queue** is designed for multithreaded environments where multiple threads may attempt to enqueue or dequeue elements simultaneously. It ensures thread-safe access to the queue.

### Operations:

- **Enqueue**: Thread-safe insertion of elements at the rear.
- **Dequeue**: Thread-safe removal of elements from the front.

---

## 9. **Double-ended Priority Queue**

A **Double-ended Priority Queue** is a combination of a priority queue and a deque, allowing both ends to function as priority queues.

### Operations:

- **Enqueue**: Insert elements based on priority.
- **Dequeue Min**: Remove the element with the smallest priority.
- **Dequeue Max**: Remove the element with the highest priority.

---

## 10. **Monotonic Queue**

A **Monotonic Queue** is a specialized queue that maintains its elements in either increasing or decreasing order. It is commonly used in sliding window algorithms for optimization.

### Operations:

- **Enqueue**: Insert elements while maintaining the monotonic property.
- **Dequeue**: Remove elements based on the monotonic order.
