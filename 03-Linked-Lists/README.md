# Linked Lists Pattern

**Author:** Ritesh Rana

## Introduction to Linked Lists

Linked Lists are fundamental linear data structures where elements are stored in nodes, and each node contains data and a reference (or pointer) to the next node in the sequence. Unlike arrays, linked list elements are not stored in contiguous memory locations, making them dynamic and flexible for insertions and deletions.

### Key Concepts

**Basic Structure:**
- **Node**: Contains data and a pointer to the next node
- **Head**: Reference to the first node in the list
- **Tail**: Reference to the last node (optional)
- **Dynamic Size**: Can grow or shrink during runtime

**Types of Linked Lists:**
1. **Singly Linked List**: Each node points to the next node
2. **Doubly Linked List**: Each node has pointers to both next and previous nodes
3. **Circular Linked List**: Last node points back to the first node

### Common Patterns

1. **Two Pointers** - Fast and slow pointers for cycle detection, finding middle
2. **Reversal** - Reversing parts or entire linked lists
3. **Merging** - Combining multiple sorted linked lists
4. **Cycle Detection** - Finding loops in linked lists
5. **Node Removal** - Removing nodes with specific conditions

### When to Use Linked Lists

- Dynamic memory allocation needed
- Frequent insertions/deletions at the beginning
- Size of data structure varies significantly
- Memory is not a constraint (linked lists have memory overhead)
- Don't need random access to elements

### Time Complexity Comparison

| Operation | Array | Linked List |
|-----------|-------|-------------|
| Access | O(1) | O(n) |
| Search | O(n) | O(n) |
| Insert at beginning | O(n) | O(1) |
| Insert at end | O(1) | O(n) without tail, O(1) with tail |
| Delete at beginning | O(n) | O(1) |
| Delete at end | O(1) | O(n) |

## Problems Covered

1. Introduction to Linked Lists
2. Linked List Reversal
3. Remove the Kth Last Node From a Linked List
4. Linked List Intersection
5. LRU Cache
6. Palindromic Linked List
7. Flatten a Multi-Level Linked List

## Interview Tips for Linked Lists

💡 **Key Interview Tips:**

1. **Draw the problem** - Visualize nodes and pointers on paper
2. **Handle edge cases** - Empty lists, single nodes, null pointers
3. **Use dummy nodes** - Simplify edge case handling
4. **Two pointer technique** - Often useful for linked list problems
5. **Consider time/space tradeoffs** - In-place vs using extra space

### Common Pitfalls and How to Avoid Them

1. **Null Pointer Exceptions**
   - Always check if node is null before accessing
   - Use defensive programming practices

2. **Memory Leaks**
   - In languages like C++, remember to delete nodes
   - Be careful with cyclic references

3. **Losing References**
   - Keep track of important nodes before modifying pointers
   - Use temporary variables when needed

### Language-Specific Implementation Notes

**Python:**
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

**Java:**
```java
class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { 
        this.val = val; 
        this.next = next; 
    }
}
```

**JavaScript:**
```javascript
function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val);
    this.next = (next===undefined ? null : next);
}
```

---
*Master linked list manipulations to solve complex interview problems efficiently!*