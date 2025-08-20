# Sort and Search Pattern

**Author:** Ritesh Rana

## Introduction to Sort and Search

Sorting and Searching are fundamental algorithmic concepts that form the backbone of many complex algorithms. Sorting arranges elements in a specific order, while searching finds specific elements in collections. Understanding various sorting algorithms and their trade-offs is crucial for optimizing performance in different scenarios.

### Key Concepts

**Sorting Fundamentals:**
- **Comparison-based**: Algorithms that use element comparisons (Merge Sort, Quick Sort)
- **Non-comparison**: Algorithms using element properties (Counting Sort, Radix Sort)
- **Stability**: Preserving relative order of equal elements
- **In-place**: Sorting without extra memory
- **Adaptive**: Performance improves with partially sorted input

**Search Fundamentals:**
- **Linear Search**: Sequential scanning through elements
- **Binary Search**: Divide-and-conquer on sorted data
- **Hash-based**: Using hash tables for constant-time lookup
- **Tree-based**: Using BST, AVL, or other tree structures

### Common Sorting Algorithms

| Algorithm | Time (Best) | Time (Average) | Time (Worst) | Space | Stable |
|-----------|-------------|----------------|--------------|-------|--------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No |

### Common Patterns

1. **Custom Comparisons** - Sorting with custom criteria
2. **Kth Element** - Finding kth largest/smallest element
3. **Partial Sorting** - Sorting only part of the array
4. **Counting Elements** - Frequency-based sorting
5. **Dutch National Flag** - Three-way partitioning
6. **Binary Search Variants** - First/last occurrence, insertion point

### When to Use Different Algorithms

**Merge Sort**: Stable sort needed, guaranteed O(n log n)
**Quick Sort**: Average case performance, in-place sorting
**Heap Sort**: Worst-case O(n log n), limited memory
**Counting Sort**: Small range of integer values
**Radix Sort**: Integer keys, linear time needed

## Problems Covered

1. Introduction to Sort and Search
2. Sort Linked List
3. Sort Array
4. Kth Largest Integer
5. Dutch National Flag

## Interview Tips for Sort and Search

💡 **Key Interview Tips:**

1. **Choose appropriate algorithm** - Consider input size, memory, stability requirements
2. **Understand trade-offs** - Time vs space, best vs worst case
3. **Handle edge cases** - Empty arrays, single elements, duplicates
4. **Consider custom comparators** - For complex objects or special ordering
5. **Think about preprocessing** - Sometimes sorting enables efficient solutions

### Implementation Examples

**Quick Sort:**
```python
def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
```

**Merge Sort:**
```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

**Quick Select (Kth Largest Element):**
```python
def find_kth_largest(nums, k):
    def quick_select(left, right, k_smallest):
        pivot_index = partition(nums, left, right)
        
        if k_smallest == pivot_index:
            return nums[pivot_index]
        elif k_smallest < pivot_index:
            return quick_select(left, pivot_index - 1, k_smallest)
        else:
            return quick_select(pivot_index + 1, right, k_smallest)
    
    return quick_select(0, len(nums) - 1, len(nums) - k)
```

**Dutch National Flag (3-way Partitioning):**
```python
def sort_colors(nums):
    """Sort array of 0s, 1s, and 2s"""
    low = mid = 0
    high = len(nums) - 1
    
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
            # Don't increment mid as we need to check swapped element
```

**Counting Sort:**
```python
def counting_sort(arr, max_val):
    # Count occurrences
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    
    # Calculate cumulative counts
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    # Build output array
    output = [0] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
    
    return output
```

**Binary Search in Rotated Array:**
```python
def search_rotated(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        # Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1
```

### Advanced Techniques

**External Sorting:**
Sorting data that doesn't fit in memory

**Parallel Sorting:**
Utilizing multiple cores for sorting

**Adaptive Sorting:**
Algorithms that perform better on partially sorted data

### Common Pitfalls and How to Avoid Them

1. **Choosing Wrong Algorithm**
   - Consider input characteristics and requirements
   - Understand when stability matters

2. **Integer Overflow in Binary Search**
   - Use `left + (right - left) // 2` instead of `(left + right) // 2`

3. **Off-by-One Errors**
   - Be careful with inclusive/exclusive bounds
   - Test with simple examples

4. **Not Handling Duplicates**
   - Consider equal elements in comparisons
   - Use stable sorts when order matters

---
*Master sorting and searching algorithms to efficiently organize and find data in various scenarios!*