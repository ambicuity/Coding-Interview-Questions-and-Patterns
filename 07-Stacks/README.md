# Stacks Pattern

**Author:** Ritesh Rana

## Introduction to Stacks

A Stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle. Elements are added and removed from the same end, called the "top" of the stack. This simple yet powerful data structure is fundamental to many algorithms and is essential for solving various programming problems.

### Key Concepts

**Basic Operations:**
- **Push**: Add element to the top of the stack
- **Pop**: Remove and return the top element
- **Peek/Top**: Return the top element without removing it
- **isEmpty**: Check if the stack is empty
- **Size**: Get the number of elements in the stack

**LIFO Principle:**
The last element added to the stack is the first one to be removed, like a stack of plates.

### Common Patterns

1. **Parentheses Matching** - Validating balanced brackets
2. **Expression Evaluation** - Evaluating postfix/prefix expressions
3. **Next Greater Element** - Finding next larger element for each element
4. **Monotonic Stack** - Maintaining elements in monotonic order
5. **Backtracking** - Storing states for backtracking algorithms
6. **Function Calls** - Managing function call stack

### When to Use Stacks

- Parsing and expression evaluation
- Backtracking algorithms
- Undo functionality
- Browser history
- Function call management
- Depth-First Search (DFS) traversals

### Time and Space Complexity

| Operation | Time Complexity |
|-----------|----------------|
| Push | O(1) |
| Pop | O(1) |
| Peek | O(1) |
| Search | O(n) |

**Space Complexity:** O(n) where n is the number of elements

## Problems Covered

1. Introduction to Stacks
2. Valid Parenthesis Expression
3. Next Largest Number to the Right
4. Evaluate Expression
5. Repeated Removal of Adjacent Duplicates
6. Implement a Queue using Stacks
7. Maximums of Sliding Window

## Interview Tips for Stacks

💡 **Key Interview Tips:**

1. **Think LIFO** - Consider if the last element needs to be processed first
2. **Pattern recognition** - Look for nested structures or matching pairs
3. **Monotonic stacks** - Great for "next greater/smaller" type problems
4. **Space vs time tradeoffs** - Stacks often trade space for time efficiency
5. **Edge cases** - Empty stacks, single elements, unbalanced inputs

### Implementation Examples

**Basic Stack Operations:**
```python
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0
```

**Valid Parentheses:**
```python
def is_valid_parentheses(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            stack.append(char)
    
    return not stack
```

### Advanced Stack Techniques

**Monotonic Stack:**
Maintains elements in monotonic (increasing/decreasing) order
```python
def next_greater_elements(nums):
    result = [-1] * len(nums)
    stack = []
    
    for i, num in enumerate(nums):
        while stack and nums[stack[-1]] < num:
            idx = stack.pop()
            result[idx] = num
        stack.append(i)
    
    return result
```

### Common Pitfalls and How to Avoid Them

1. **Stack Underflow**
   - Always check if stack is empty before popping
   - Handle edge cases properly

2. **Memory Management**
   - Be aware of stack size limitations
   - Clean up when using manual memory management

3. **Incorrect Matching Logic**
   - Ensure proper pairing logic for parentheses problems
   - Test with various input combinations

---
*Master stack operations to solve parsing, evaluation, and backtracking problems efficiently!*