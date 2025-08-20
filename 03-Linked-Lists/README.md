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

1. **Draw the problem** - Visualize nodes and pointers on paper/whiteboard
2. **Handle edge cases** - Empty lists, single nodes, null pointers, cycles
3. **Use dummy nodes** - Simplify edge case handling for insertions/deletions
4. **Two pointer technique** - Fast/slow pointers for many problems
5. **Consider time/space tradeoffs** - In-place vs using extra space
6. **Plan pointer updates** - Think through the order of pointer modifications
7. **Test with examples** - Walk through small examples step by step

### Essential Linked List Patterns

**1. Dummy Node Pattern:**
```python
def remove_elements(head, val):
    dummy = ListNode(0)
    dummy.next = head
    current = dummy
    
    while current.next:
        if current.next.val == val:
            current.next = current.next.next
        else:
            current = current.next
    
    return dummy.next
```

**2. Two Pointer Technique:**
```python
def find_middle(head):
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow  # Middle node
```

**3. Reverse Linked List:**
```python
def reverse_list(head):
    prev = None
    current = head
    
    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp
    
    return prev
```

**4. Merge Two Sorted Lists:**
```python
def merge_two_lists(list1, list2):
    dummy = ListNode(0)
    current = dummy
    
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    current.next = list1 or list2
    return dummy.next
```

**5. Cycle Detection (Floyd's Algorithm):**
```python
def has_cycle(head):
    if not head or not head.next:
        return False
    
    slow = head
    fast = head.next
    
    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next
    
    return True
```

### Advanced Techniques

**Remove Nth Node from End:**
```python
def remove_nth_from_end(head, n):
    dummy = ListNode(0)
    dummy.next = head
    
    # Move first pointer n+1 steps ahead
    first = dummy
    for _ in range(n + 1):
        first = first.next
    
    # Move both pointers until first reaches end
    second = dummy
    while first:
        first = first.next
        second = second.next
    
    # Remove nth node from end
    second.next = second.next.next
    return dummy.next
```

**Partition List:**
```python
def partition(head, x):
    before_head = ListNode(0)
    after_head = ListNode(0)
    
    before = before_head
    after = after_head
    
    while head:
        if head.val < x:
            before.next = head
            before = before.next
        else:
            after.next = head
            after = after.next
        head = head.next
    
    after.next = None
    before.next = after_head.next
    
    return before_head.next
```

**Copy List with Random Pointer:**
```python
def copy_random_list(head):
    if not head:
        return None
    
    # Step 1: Create new nodes and insert them
    current = head
    while current:
        new_node = ListNode(current.val)
        new_node.next = current.next
        current.next = new_node
        current = new_node.next
    
    # Step 2: Set random pointers
    current = head
    while current:
        if current.random:
            current.next.random = current.random.next
        current = current.next.next
    
    # Step 3: Separate the lists
    dummy = ListNode(0)
    new_current = dummy
    current = head
    
    while current:
        new_current.next = current.next
        current.next = current.next.next
        current = current.next
        new_current = new_current.next
    
    return dummy.next
```

### Common Pitfalls and How to Avoid Them

1. **Null Pointer Exceptions**
   - Always check if node is null before accessing: `if (node != null)`
   - Use defensive programming practices
   - Check both `node` and `node.next` when needed

2. **Memory Leaks**
   - In languages like C++, remember to delete nodes properly
   - Be careful with cyclic references in languages without garbage collection
   - Break cycles before deletion

3. **Losing References**
   - Keep track of important nodes before modifying pointers
   - Use temporary variables: `temp = current.next`
   - Plan the order of pointer updates carefully

4. **Off-by-One Errors**
   - Be careful with loop conditions and pointer movements
   - Test with edge cases: empty list, single node, two nodes
   - Use clear variable naming: `prev`, `current`, `next`

5. **Incorrect Dummy Node Usage**
   - Remember to return `dummy.next`, not `dummy`
   - Initialize dummy node properly: `dummy = ListNode(0)`
   - Don't modify the dummy node after setting it up

### Advanced Problem-Solving Strategies

**When to Use Each Approach:**

| Problem Type | Best Approach | Example |
|--------------|---------------|---------|
| Finding middle | Two pointers (fast/slow) | Middle of linked list |
| Cycle detection | Floyd's cycle detection | Detect loop |
| Reversing | Iterative with three pointers | Reverse linked list |
| Merging | Two pointers with dummy | Merge sorted lists |
| Removing nodes | Dummy node + traversal | Remove duplicates |
| Copying | Clone then separate | Copy with random pointer |
| K-way operations | Divide and conquer | Merge K sorted lists |

**Optimization Techniques:**

1. **Space Optimization**: Modify in-place when possible
2. **Time Optimization**: Use two pointers to avoid multiple passes
3. **Code Clarity**: Use meaningful variable names and comments
4. **Edge Case Handling**: Always consider empty and single-node lists

### Testing Strategy for Linked List Problems

**Essential Test Cases:**
```python
# Test case templates for linked list problems
test_cases = [
    # Edge cases
    None,                    # Empty list
    [1],                     # Single node
    [1, 2],                  # Two nodes
    
    # Normal cases
    [1, 2, 3, 4, 5],        # Multiple nodes
    [1, 1, 2, 2, 3],        # Duplicates
    
    # Special cases
    [1, 2, 3, 2, 1],        # Palindrome
    # Cyclic list (requires special construction)
]

def test_linked_list_function(func, test_cases):
    for i, case in enumerate(test_cases):
        if case is None:
            result = func(None)
        else:
            head = build_linked_list(case)
            result = func(head)
        
        print(f"Test {i}: Input={case}, Output={linked_list_to_array(result)}")
```

**Performance Benchmarking:**
```python
import time

def benchmark_linked_list_operation(operation, sizes=[100, 1000, 10000]):
    for size in sizes:
        # Create linked list of given size
        head = create_linked_list(size)
        
        start_time = time.time()
        result = operation(head)
        end_time = time.time()
        
        print(f"Size {size}: {end_time - start_time:.4f} seconds")
```

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