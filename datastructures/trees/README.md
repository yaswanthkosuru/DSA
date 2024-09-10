# Trees in Data Structures and Algorithms (DSA)

**Trees** are non linear data structures that consist of **nodes** connected by **edges** and maintain parent child relation ship.

## Glossary of Trees

1. **Node**: A basic unit of a tree which has left and right pointers.
2. **Root**: the top most node in tree.
3. **Edge**: A link between two nodes.
4. **Child**: A node that is a direct descendant of another node.
5. **Parent**: A node that has children.
6. **Leaf Node**: A node that does not have any children (also called a terminal node).
7. **Subtree**: A tree consisting of a node and its descendants.
8. **Height of a Node**: The number of edges on the longest path from that node to a leaf.
9. **Depth of a Node**: The number of edges from the root to the node.
10. **Degree of a Node**: The number of children a node has.

## Types of Trees in DSA

## 1. **Binary Tree**

- A tree where each node has at most two children (left and right).
- **full binary tree**(0 or 2 nodes),
- **complete binary tree** (fill from left),
- **perfect binary tree** (2 children and same level)

## 2. **Binary Search Tree (BST)**

- A binary tree where the left child of a node contains values smaller than the node, and the right child contains values greater than the node.

## 3. **Balanced Tree**

- A tree in which the height of the left and right subtrees of any node differs by no more than one.

## 4. **AVL Tree**

- A self-balancing binary search tree where the difference in heights of left and right subtrees cannot be more than one.

## 5. **Red-Black Tree**

- A self-balancing binary search tree where each node is either red or black, ensuring the tree remains balanced.

## 6. **Heap**

- A complete binary tree used for priority queues, where:
- **Max Heap**: The parent node is greater than or equal to its children.
- **Min Heap**: The parent node is smaller than or equal to its children.

## 7. **N-ary Tree**

- A tree where each node can have up to **N** children.

## 8. **Trie (Prefix Tree)**

- A tree used for storing strings, where each node represents a single character, often used in autocomplete systems.

## 9. **Segment Tree**

- A binary tree used for storing intervals or segments. It allows querying which segments contain a given point.

## 10. **Fenwick Tree (Binary Indexed Tree)**

- A data structure that provides efficient methods for calculating prefix sums and updating the data.

## 11. **B-Tree**

- A self-balancing search tree in which nodes can have multiple children and is optimized for systems that read and write large blocks of data.

## 12. **B+ Tree**

- A variant of the B-tree where all values are stored in leaf nodes, and internal nodes only store keys for searching.

## 13. **Suffix Tree**

- A compressed trie of all suffixes of a given string. It's used in string processing, pattern matching, and bioinformatics.

## 14. **Spanning Tree**

- A subgraph of a graph that connects all the vertices together without cycles and with the minimum possible number of edges.

## 15. **Decision Tree**

- A tree used in machine learning for classification and regression tasks. Each node represents a decision based on features.

## 16. **K-D Tree (K-Dimensional Tree)**

- A tree used for organizing points in a k-dimensional space, often used in searches involving multidimensional keys.

## 17. **Ternary Tree**

- A tree where each node has at most three children.

## 18. **Van Emde Boas Tree (vEB Tree)**

- A tree structure that provides fast operations for a universe of size **U** and is used in dynamic order statistics and predecessor/successor queries.

## 19. **Binary Space Partitioning Tree (BSP Tree)**

- A tree used in computer graphics and computational geometry to represent partitions of space.

## 20. **Quadtree**

- A tree where each internal node has exactly four children, often used to partition a two-dimensional space.

## 21. **Octree**

- A tree where each internal node has eight children, used to partition a three-dimensional space.

## 22. **Splay Tree**

- A self-adjusting binary search tree where recently accessed elements are moved to the root.

## 23. **R-Tree**

- A tree used for indexing multi-dimensional information like geographical coordinates.

## 24. **Expression Tree**

- A binary tree used to represent arithmetic expressions, where leaves are operands and internal nodes are operators.

## 25. **Huffman Tree**

- A tree used in data compression algorithms (Huffman coding) to represent variable-length codes for symbols.
