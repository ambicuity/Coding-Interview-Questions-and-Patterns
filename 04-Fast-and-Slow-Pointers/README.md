# Fast and Slow Pointers Pattern

**Author:** Ritesh Rana

## Introduction to Fast and Slow Pointers

The Fast and Slow Pointers technique, also known as Floyd's Tortoise and Hare algorithm, is a powerful two-pointer approach where one pointer moves faster than the other. This technique is particularly useful for solving problems involving cycles in linked lists and finding specific positions without knowing the length of the data structure.

### Key Concepts

**Basic Principle:**
- **Slow Pointer**: Moves one step at a time
- **Fast Pointer**: Moves two steps at a time
- **Meeting Point**: When fast and slow pointers meet, it indicates a cycle
- **Cycle Detection**: If fast pointer reaches null, no cycle exists

**Common Speed Ratios:**
1. **1:2 Ratio** - Most common (slow moves 1, fast moves 2)
2. **1:3 Ratio** - Less common but useful in specific cases
3. **Variable Speed** - Speed changes based on conditions

### Common Patterns

1. **Cycle Detection** - Detecting loops in linked lists
2. **Finding Middle** - Locating the middle element
3. **Cycle Length** - Calculating the length of a cycle
4. **Cycle Start** - Finding where the cycle begins
5. **Happy Numbers** - Detecting cycles in number sequences

### When to Use Fast and Slow Pointers

- Detecting cycles in linked lists
- Finding the middle of a linked list
- Detecting patterns in sequences
- Memory-efficient solutions (O(1) space)
- Problems involving "meeting points"

### Time and Space Complexity

**Time Complexity:** O(n) - Each element visited at most twice
**Space Complexity:** O(1) - Only using two pointers

## Problems Covered

1. Introduction to Fast and Slow Pointers
2. Linked List Loop
3. Linked List Midpoint  
4. Happy Number

## Interview Tips for Fast and Slow Pointers

💡 **Key Interview Tips:**

1. **Visualize the movement** - Draw how pointers move through the structure
2. **Consider edge cases** - Empty lists, single nodes, no cycles
3. **Understand the math** - Why fast/slow pointers work for cycle detection
4. **Start simple** - Begin with basic cycle detection, then extend
5. **Practice variations** - Different speed ratios and applications

### Algorithm Analysis

**Why Fast and Slow Pointers Work for Cycle Detection:**
- If there's no cycle, fast pointer will reach the end
- If there's a cycle, fast pointer will eventually "lap" the slow pointer
- The meeting point guarantees cycle existence

**Finding Cycle Start:**
1. Detect cycle using fast/slow pointers
2. Keep slow pointer at meeting point
3. Move another pointer from start at same speed as slow
4. Where they meet is the cycle start

### Common Pitfalls and How to Avoid Them

1. **Null Pointer Exceptions**
   - Always check if fast and fast.next exist before moving
   - Handle empty and single-node lists

2. **Infinite Loops**
   - Ensure proper termination conditions
   - Check for null pointers in each iteration

3. **Off-by-One Errors**
   - Be careful with pointer movements and stopping conditions
   - Test with simple examples first

### Implementation Template

```python
def has_cycle(head):
    if not head or not head.next:
        return False
    
    slow = head
    fast = head.next
    
    while fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next
    
    return False
```

---
*Master the fast and slow pointers technique for elegant cycle detection solutions!*