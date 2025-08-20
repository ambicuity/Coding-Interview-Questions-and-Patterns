# Binary Search Pattern

**Author:** Ritesh Rana

## Introduction to Binary Search

Binary Search is a powerful divide-and-conquer algorithm used to find a target element in a sorted array or to find the insertion point for an element. It works by repeatedly dividing the search space in half, eliminating half of the remaining elements in each step.

### Key Concepts

**Basic Principle:**
- **Sorted Data**: Binary search requires sorted input
- **Divide and Conquer**: Split search space in half each iteration
- **Logarithmic Time**: O(log n) time complexity
- **Comparison-Based**: Uses comparisons to narrow search space

**Core Algorithm:**
1. Compare target with middle element
2. If equal, return the index
3. If target is smaller, search left half
4. If target is larger, search right half
5. Repeat until found or search space is empty

### Common Patterns

1. **Standard Binary Search** - Finding exact element
2. **First/Last Occurrence** - Finding boundaries in sorted array with duplicates
3. **Insertion Point** - Finding where to insert element to maintain sorted order
4. **Search in Rotated Array** - Modified binary search for rotated sorted arrays
5. **Peak Finding** - Finding local maxima in arrays
6. **Square Root** - Finding integer square root using binary search

### When to Use Binary Search

- Searching in sorted arrays
- Finding insertion points
- Optimization problems with monotonic functions
- Finding boundaries in sorted data
- Problems that can be reduced to "yes/no" questions

### Time and Space Complexity

**Time Complexity:** O(log n)
**Space Complexity:** O(1) iterative, O(log n) recursive

## Problems Covered

1. Introduction to Binary Search
2. Find the Insertion Index
3. First and Last Occurrences of a Number
4. Cutting Wood
5. Find the Target in a Rotated Sorted Array
6. Find the Median From Two Sorted Arrays
7. Matrix Search
8. Local Maxima in Array
9. Weighted Random Selection

## Interview Tips for Binary Search

💡 **Key Interview Tips:**

1. **Check if data is sorted** - Binary search requires sorted input
2. **Handle edge cases** - Empty arrays, single elements, target not found
3. **Choose correct boundaries** - Be careful with inclusive/exclusive bounds
4. **Avoid infinite loops** - Ensure search space decreases each iteration
5. **Consider variations** - First/last occurrence, insertion point, etc.

### Implementation Template

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Not found
```

### Common Variations

**Find First Occurrence:**
```python
def find_first(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Continue searching left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result
```

### Common Pitfalls and How to Avoid Them

1. **Integer Overflow**
   - Use `mid = left + (right - left) // 2` instead of `(left + right) // 2`

2. **Infinite Loops**
   - Ensure loop termination with proper boundary updates
   - Use correct comparison operators

3. **Off-by-One Errors**
   - Be careful with inclusive/exclusive boundaries
   - Test with simple examples

---
*Master binary search to efficiently solve searching and optimization problems!*