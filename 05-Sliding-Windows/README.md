# Sliding Windows Pattern

**Author:** Ritesh Rana

## Introduction to Sliding Windows

The Sliding Window technique is an algorithmic pattern used to perform operations on a specific window size of a data structure, typically arrays or strings. Instead of recalculating everything from scratch for each window, this technique efficiently slides the window by removing elements from one end and adding elements to the other end.

### Key Concepts

**Basic Principle:**
- **Window**: A contiguous subarray or substring of fixed or variable size
- **Sliding**: Moving the window by adding/removing elements
- **Optimization**: Avoid redundant calculations by reusing previous results

**Types of Sliding Windows:**
1. **Fixed Size Window** - Window size remains constant
2. **Variable Size Window** - Window size changes based on conditions
3. **Multi-Window** - Multiple windows slide simultaneously

### Common Patterns

1. **Fixed Window Size** - Maximum sum of k consecutive elements
2. **Variable Window** - Longest substring with unique characters
3. **Shrinking Window** - Minimum window containing all characters
4. **Expanding Window** - Growing window until condition breaks
5. **Frequency Counting** - Track character frequencies in current window

### When to Use Sliding Windows

- Problems involving subarrays or substrings
- Finding maximum/minimum values in windows
- Optimization problems with contiguous elements
- Avoiding nested loops for better time complexity
- Pattern matching and frequency counting

### Time Complexity Benefits

**Without Sliding Window:** O(n*k) or O(n²)
**With Sliding Window:** O(n)

The technique reduces time complexity by eliminating redundant calculations.

## Problems Covered

1. Introduction to Sliding Windows
2. Substring Anagrams
3. Longest Substring With Unique Characters
4. Longest Uniform Substring After Replacements

## Interview Tips for Sliding Windows

💡 **Key Interview Tips:**

1. **Identify the pattern** - Look for contiguous subarray/substring problems
2. **Choose window type** - Fixed vs variable size based on problem
3. **Track window state** - Use hashmaps for frequency counting
4. **Handle edge cases** - Empty arrays, single elements
5. **Optimize incrementally** - Start with brute force, then apply sliding window

### Implementation Patterns

**Fixed Size Window:**
```python
def max_sum_subarray(arr, k):
    if len(arr) < k:
        return -1
    
    # Calculate sum of first window
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Slide the window
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum
```

**Variable Size Window:**
```python
def longest_unique_substring(s):
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length
```

### Common Pitfalls and How to Avoid Them

1. **Window Size Validation**
   - Check if array size is smaller than window size
   - Handle empty arrays and single elements

2. **Index Management**
   - Be careful with left and right pointers
   - Avoid index out of bounds errors

3. **State Management**
   - Properly update window state when sliding
   - Reset counters and data structures when needed

### Advanced Techniques

**Multiple Conditions:**
- Track multiple constraints simultaneously
- Use multiple hashmaps for different criteria

**Optimization Strategies:**
- Early termination when optimal solution found
- Precompute values when possible
- Use appropriate data structures (deque for min/max)

---
*Master the sliding window technique to efficiently solve array and string problems!*