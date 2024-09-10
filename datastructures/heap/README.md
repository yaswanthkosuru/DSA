# Types of Stacks in DSA

## Key Operations

- **Push**: Add an element to the top of the stack.
- **Pop**: Remove the top element.
- **Peek/Top**: Get the top element without removing it.
  
---

## 1. **Array-based Stack**

An **Array-based Stack** uses an array to implement the stack data structure. It has a fixed size, and elements are added or removed from the top of the stack.

## 2. **Linked List-based Stack**

A **Linked List-based Stack** uses a linked list to implement the stack, allowing dynamic resizing. Each element (node) points to the next, and elements are added or removed from the head of the list.

## 6. **Monotonic Stack**

A **Monotonic Stack** is a special type of stack where the elements are either in non-increasing or non-decreasing order. It is commonly used in problems involving ranges, like finding the next greater element.

## 7. **Threaded Stack**

A **Threaded Stack** is designed for use in multi-threaded environments where multiple threads may try to push or pop simultaneously. It ensures thread safety, usually using locks or atomic operations.

## 8. **Call Stack**

The **Call Stack** is a special stack used in programming to keep track of active function calls in a program. Each time a function is called, its execution context is pushed onto the stack, and when the function returns, it is popped.
