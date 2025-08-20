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

1. **Verify sorted input** - Binary search requires sorted data (or rotated sorted)
2. **Handle edge cases systematically** - Empty arrays, single elements, target not found
3. **Choose correct template** - Standard search vs first/last occurrence vs insertion point
4. **Avoid integer overflow** - Use `left + (right - left) // 2` for mid calculation
5. **Master boundary management** - Understand when to use inclusive vs exclusive bounds
6. **Think beyond arrays** - Binary search applies to any monotonic function
7. **Practice common variants** - Rotated arrays, 2D matrices, optimization problems

### Comprehensive Binary Search Templates

**1. Standard Binary Search:**
```python
def binary_search_iterative(arr, target):
    """Standard binary search - finds any occurrence of target"""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def binary_search_recursive(arr, target, left=0, right=None):
    """Recursive implementation of binary search"""
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = left + (right - left) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)
```

**2. First and Last Occurrence:**
```python
def find_first_occurrence(arr, target):
    """Find the first occurrence of target in sorted array with duplicates"""
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Continue searching in left half
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result

def find_last_occurrence(arr, target):
    """Find the last occurrence of target in sorted array with duplicates"""
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            result = mid
            left = mid + 1  # Continue searching in right half
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result

def find_range(arr, target):
    """Find first and last occurrence of target"""
    first = find_first_occurrence(arr, target)
    if first == -1:
        return [-1, -1]
    
    last = find_last_occurrence(arr, target)
    return [first, last]
```

**3. Insertion Point and Bounds:**
```python
def find_insertion_point(arr, target):
    """Find the insertion point to maintain sorted order"""
    left, right = 0, len(arr)
    
    while left < right:
        mid = left + (right - left) // 2
        
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left

def lower_bound(arr, target):
    """Find first position where element >= target"""
    left, right = 0, len(arr)
    
    while left < right:
        mid = left + (right - left) // 2
        
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left

def upper_bound(arr, target):
    """Find first position where element > target"""
    left, right = 0, len(arr)
    
    while left < right:
        mid = left + (right - left) // 2
        
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    
    return left
```

**4. Advanced Binary Search Applications:**
```python
# Search in rotated sorted array
def search_rotated_array(arr, target):
    """Search target in rotated sorted array"""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        
        # Left half is sorted
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1

# Find minimum in rotated sorted array
def find_min_rotated(arr):
    """Find minimum element in rotated sorted array"""
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        
        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid
    
    return arr[left]

# Search in 2D matrix
def search_matrix(matrix, target):
    """Search target in row-wise and column-wise sorted matrix"""
    if not matrix or not matrix[0]:
        return False
    
    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        row = mid // cols
        col = mid % cols
        
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False

# Find peak element
def find_peak_element(arr):
    """Find any peak element in array"""
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        
        if arr[mid] > arr[mid + 1]:
            right = mid
        else:
            left = mid + 1
    
    return left

# Square root using binary search
def integer_square_root(x):
    """Find integer square root using binary search"""
    if x < 2:
        return x
    
    left, right = 1, x // 2
    
    while left <= right:
        mid = left + (right - left) // 2
        square = mid * mid
        
        if square == x:
            return mid
        elif square < x:
            left = mid + 1
        else:
            right = mid - 1
    
    return right  # Floor of square root
```

**5. Optimization Problems with Binary Search:**
```python
# Capacity to ship packages within D days
def ship_within_days(weights, days):
    """Find minimum ship capacity to ship all packages within D days"""
    def can_ship(capacity):
        current_weight = 0
        days_needed = 1
        
        for weight in weights:
            if current_weight + weight > capacity:
                days_needed += 1
                current_weight = weight
            else:
                current_weight += weight
        
        return days_needed <= days
    
    left = max(weights)  # Minimum possible capacity
    right = sum(weights)  # Maximum possible capacity
    
    while left < right:
        mid = left + (right - left) // 2
        
        if can_ship(mid):
            right = mid
        else:
            left = mid + 1
    
    return left

# Koko eating bananas
def min_eating_speed(piles, h):
    """Find minimum eating speed to finish all bananas in h hours"""
    def can_finish(speed):
        total_time = 0
        for pile in piles:
            total_time += (pile + speed - 1) // speed  # Ceiling division
        return total_time <= h
    
    left, right = 1, max(piles)
    
    while left < right:
        mid = left + (right - left) // 2
        
        if can_finish(mid):
            right = mid
        else:
            left = mid + 1
    
    return left

# Split array into m subarrays with minimum largest sum
def split_array(nums, m):
    """Split array into m subarrays minimizing the largest sum"""
    def can_split(max_sum):
        count = 1
        current_sum = 0
        
        for num in nums:
            if current_sum + num > max_sum:
                count += 1
                current_sum = num
                if count > m:
                    return False
            else:
                current_sum += num
        
        return True
    
    left = max(nums)  # Minimum possible max sum
    right = sum(nums)  # Maximum possible max sum
    
    while left < right:
        mid = left + (right - left) // 2
        
        if can_split(mid):
            right = mid
        else:
            left = mid + 1
    
    return left
```

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

### Advanced Binary Search Patterns and Techniques

**1. Binary Search on Answer (Optimization):**
```python
def binary_search_on_answer_template(search_space_start, search_space_end, condition_func):
    """
    Template for binary search on answer pattern
    Used when we want to find optimal value in a monotonic function
    """
    left, right = search_space_start, search_space_end
    
    while left < right:
        mid = left + (right - left) // 2
        
        if condition_func(mid):
            right = mid  # mid is feasible, try smaller
        else:
            left = mid + 1  # mid is not feasible, need larger
    
    return left

# Example: Find minimum reading speed
def min_reading_speed(books, max_time):
    def can_finish(speed):
        total_time = sum((book + speed - 1) // speed for book in books)
        return total_time <= max_time
    
    return binary_search_on_answer_template(1, max(books), can_finish)
```

**2. Fractional Binary Search:**
```python
def fractional_binary_search(func, target, precision=1e-6):
    """Binary search on continuous space"""
    left, right = 0.0, 1000.0
    
    while right - left > precision:
        mid = (left + right) / 2
        
        if func(mid) < target:
            left = mid
        else:
            right = mid
    
    return (left + right) / 2

# Example: Find cube root
def cube_root(x):
    def cube(n):
        return n ** 3
    
    if x >= 0:
        return fractional_binary_search(cube, x)
    else:
        return -fractional_binary_search(cube, -x)
```

**3. Multi-dimensional Binary Search:**
```python
def search_matrix_ii(matrix, target):
    """Search in matrix where rows and columns are sorted"""
    if not matrix or not matrix[0]:
        return False
    
    row, col = 0, len(matrix[0]) - 1
    
    while row < len(matrix) and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            col -= 1
        else:
            row += 1
    
    return False

def find_kth_smallest_in_matrix(matrix, k):
    """Find kth smallest element in row-wise and column-wise sorted matrix"""
    def count_less_equal(mid):
        count = 0
        row = len(matrix) - 1
        col = 0
        
        while row >= 0 and col < len(matrix[0]):
            if matrix[row][col] <= mid:
                count += row + 1
                col += 1
            else:
                row -= 1
        
        return count
    
    left = matrix[0][0]
    right = matrix[-1][-1]
    
    while left < right:
        mid = left + (right - left) // 2
        
        if count_less_equal(mid) < k:
            left = mid + 1
        else:
            right = mid
    
    return left
```

### Problem Classification and Strategy Guide

**Binary Search Problem Types:**

| Category | Pattern | Key Insight | Template |
|----------|---------|-------------|----------|
| Direct Search | Find exact element | Sorted array | Standard binary search |
| Boundary Search | First/last occurrence | Handle duplicates | Modified comparison |
| Insertion Point | Where to insert | Maintain order | Left-biased search |
| Rotated Array | Modified sorted | Find pivot point | Conditional search |
| 2D Search | Matrix problems | Row/column properties | Coordinate mapping |
| Optimization | Min/max value | Monotonic function | Search on answer |

**Decision Tree for Binary Search Problems:**

```
Is the problem about searching/optimization?
├── Yes: Can you define a monotonic condition?
│   ├── Yes: Binary search applies
│   │   ├── Direct element search → Standard template
│   │   ├── Boundary finding → First/last template
│   │   ├── Insertion point → Lower/upper bound
│   │   └── Optimization → Search on answer
│   └── No: Consider other approaches
└── No: Different pattern needed
```

### Common Pitfalls and Expert Solutions

1. **Integer Overflow Prevention**
   ```python
   # ❌ Wrong: Can overflow for large values
   mid = (left + right) // 2
   
   # ✅ Correct: Prevents overflow
   mid = left + (right - left) // 2
   ```

2. **Infinite Loop Prevention**
   ```python
   # ❌ Wrong: Can create infinite loop
   while left <= right:
       mid = left + (right - left) // 2
       if condition(mid):
           right = mid  # Should be mid - 1
       else:
           left = mid   # Should be mid + 1
   
   # ✅ Correct: Ensures progress
   while left < right:
       mid = left + (right - left) // 2
       if condition(mid):
           right = mid
       else:
           left = mid + 1
   ```

3. **Boundary Condition Handling**
   ```python
   # For first occurrence
   def find_first_correct(arr, target):
       left, right = 0, len(arr) - 1
       result = -1
       
       while left <= right:
           mid = left + (right - left) // 2
           if arr[mid] == target:
               result = mid
               right = mid - 1  # Continue left
           elif arr[mid] < target:
               left = mid + 1
           else:
               right = mid - 1
       
       return result
   ```

### Performance Analysis and Optimization

**Time Complexity Analysis:**
- **Standard Binary Search**: O(log n)
- **Range Queries**: O(log n) per query
- **2D Matrix Search**: O(log(mn)) or O(m + n)
- **Optimization Problems**: O(log(range) * verification_time)

**Space Complexity:**
- **Iterative**: O(1)
- **Recursive**: O(log n) for call stack
- **With additional data structures**: Problem dependent

**Optimization Techniques:**

1. **Early Termination**
   ```python
   def optimized_search(arr, target):
       if not arr:
           return -1
       
       # Quick checks
       if target < arr[0] or target > arr[-1]:
           return -1
       
       # Standard binary search
       return binary_search(arr, target)
   ```

2. **Cache-Friendly Implementation**
   ```python
   def cache_friendly_search(arr, target):
       # Process in blocks for better cache locality
       block_size = 32
       for i in range(0, len(arr), block_size):
           block_end = min(i + block_size, len(arr))
           if arr[i] <= target <= arr[block_end - 1]:
               return binary_search(arr[i:block_end], target) + i
       return -1
   ```

### Testing and Validation Framework

**Comprehensive Test Suite:**
```python
def test_binary_search_comprehensive():
    """Comprehensive test suite for binary search implementations"""
    
    test_cases = [
        # Edge cases
        ([], 1, -1, "Empty array"),
        ([1], 1, 0, "Single element found"),
        ([1], 2, -1, "Single element not found"),
        
        # Normal cases
        ([1, 2, 3, 4, 5], 3, 2, "Element in middle"),
        ([1, 2, 3, 4, 5], 1, 0, "First element"),
        ([1, 2, 3, 4, 5], 5, 4, "Last element"),
        ([1, 2, 3, 4, 5], 6, -1, "Element too large"),
        ([1, 2, 3, 4, 5], 0, -1, "Element too small"),
        
        # Duplicates
        ([1, 2, 2, 2, 3], 2, [1, 3], "Multiple occurrences"),
        ([1, 1, 1, 1, 1], 1, [0, 4], "All same elements"),
        
        # Large arrays
        (list(range(1000000)), 500000, 500000, "Large array"),
    ]
    
    for arr, target, expected, description in test_cases:
        # Test different implementations
        implementations = [
            ("Standard", binary_search_iterative),
            ("Recursive", binary_search_recursive),
            ("First occurrence", find_first_occurrence),
            ("Last occurrence", find_last_occurrence),
        ]
        
        for name, func in implementations:
            try:
                result = func(arr, target)
                status = "PASS" if validate_result(result, expected, name) else "FAIL"
                print(f"{name} - {description}: {status}")
            except Exception as e:
                print(f"{name} - {description}: ERROR - {e}")

def validate_result(result, expected, func_name):
    """Validate results based on function type"""
    if isinstance(expected, list):  # Range expected
        return expected[0] <= result <= expected[1] if result != -1 else False
    else:
        return result == expected
```

---
*Master binary search to efficiently solve searching and optimization problems with logarithmic complexity!*