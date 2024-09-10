# Types of Linked Lists in DSA

---

## Operations

- **Insertion**: Insert at the beginning, end, or any position.
- **Deletion**: Remove nodes from the list.
- **Traversal**: Move through the list from the first node to the last.
- **Reverse**: Reverse the list from last to first.

---

## 1. **Singly Linked List**

A **Singly Linked List** is the most basic type of linked list, where each node points to the next node in the sequence. The last node points to `null`, marking the end of the list.

## Structure

- Each node contains:
  - **Data**: The value stored in the node.
  - **Next**: A pointer to the next node in the list.

## 2. **Doubly Linked List**

A **Doubly Linked List** allows traversal in both directions, forward and backward. Each node contains a reference to both the next and the previous node.

### Structure 

- Each node contains:
  - **Data**: The value stored in the node.
  - **Next**: A pointer to the next node.
  - **Previous**: A pointer to the previous node.

---

## 3. **Circular Linked List**

A **Circular Linked List** is a variation where the last node points back to the first node, forming a circular loop. This can be implemented as a singly or doubly linked list.

### Structure 

- **Singly Circular Linked List**: The last node's `next` pointer points to the first node.
- **Doubly Circular Linked List**: The last node's `next` pointer points to the first node, and the first node's `previous` pointer points to the last node.

---

## 4. **Circular Doubly Linked List**

A **Circular Doubly Linked List** combines both the circular and doubly linked list structures. Each node has pointers to both the next and previous nodes, and the last node connects back to the first node.

### Structure

- Each node contains:
  - **Data**: The value stored in the node.
  - **Next**: A pointer to the next node.
  - **Previous**: A pointer to the previous node.
  - The **last node's next pointer** points to the first node.
  - The **first node's previous pointer** points to the last node.

---

