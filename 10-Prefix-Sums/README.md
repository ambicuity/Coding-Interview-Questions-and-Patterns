# Prefix Sums Pattern

**Author:** Ritesh Rana

## Introduction to Prefix Sums

Prefix Sums (also known as Cumulative Sums) is a preprocessing technique that allows for efficient calculation of range sums in arrays. By precomputing the sum of elements from the beginning of the array to each position, we can answer range sum queries in constant time.

### Key Concepts

**Basic Principle:**
- **Prefix Sum**: Sum of elements from index 0 to index i
- **Range Sum**: Sum of elements between any two indices
- **Preprocessing**: Build prefix sum array once, use multiple times
- **Space-Time Tradeoff**: Use O(n) extra space for O(1) query time

**Formula:**
- `prefix[i] = arr[0] + arr[1] + ... + arr[i]`
- `range_sum(i, j) = prefix[j] - prefix[i-1]`

### Common Patterns

1. **1D Prefix Sums** - Range sums in arrays
2. **2D Prefix Sums** - Rectangle sums in matrices
3. **Difference Arrays** - Efficient range updates
4. **Subarray Sums** - Finding subarrays with target sum
5. **Moving Averages** - Sliding window averages
6. **Cumulative Frequencies** - Frequency-based calculations

### When to Use Prefix Sums

- Multiple range sum queries on static arrays
- Subarray sum problems
- Moving averages and sliding windows
- 2D matrix range queries
- Optimization problems involving cumulative values
- Statistical calculations over ranges

### Time and Space Complexity

**Preprocessing:** O(n) time, O(n) space
**Range Query:** O(1) time
**Overall:** Much faster than O(n) per query for multiple queries

## Problems Covered

1. Introduction to Prefix Sums
2. Sum Between Range
3. K-Sum Subarrays
4. Product Array Without Current Element

## Interview Tips for Prefix Sums

💡 **Key Interview Tips:**

1. **Identify range queries** - Multiple queries suggest prefix sums
2. **Handle edge cases** - Empty ranges, single elements, negative numbers
3. **Consider 2D extension** - For matrix problems, use 2D prefix sums
4. **Think about updates** - Static vs dynamic data affects approach
5. **Combine with hashmaps** - For subarray sum problems

### Implementation Examples

**1D Prefix Sum:**
```python
class PrefixSum:
    def __init__(self, arr):
        self.prefix = [0] * (len(arr) + 1)
        for i in range(len(arr)):
            self.prefix[i + 1] = self.prefix[i] + arr[i]
    
    def range_sum(self, left, right):
        """Sum of elements from index left to right (inclusive)"""
        return self.prefix[right + 1] - self.prefix[left]
```

**Subarray Sum Equals K:**
```python
def subarray_sum_k(nums, k):
    count = 0
    prefix_sum = 0
    sum_count = {0: 1}  # Handle subarrays starting from index 0
    
    for num in nums:
        prefix_sum += num
        
        # Check if there's a previous prefix sum such that
        # current_sum - previous_sum = k
        if prefix_sum - k in sum_count:
            count += sum_count[prefix_sum - k]
        
        sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1
    
    return count
```

**2D Prefix Sum:**
```python
class Matrix2DPrefixSum:
    def __init__(self, matrix):
        if not matrix or not matrix[0]:
            return
        
        m, n = len(matrix), len(matrix[0])
        self.prefix = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.prefix[i][j] = (matrix[i-1][j-1] + 
                                   self.prefix[i-1][j] + 
                                   self.prefix[i][j-1] - 
                                   self.prefix[i-1][j-1])
    
    def sum_region(self, row1, col1, row2, col2):
        """Sum of rectangle from (row1,col1) to (row2,col2)"""
        return (self.prefix[row2+1][col2+1] - 
                self.prefix[row1][col2+1] - 
                self.prefix[row2+1][col1] + 
                self.prefix[row1][col1])
```

### Advanced Techniques

**Product Array:**
```python
def product_except_self(nums):
    n = len(nums)
    result = [1] * n
    
    # Left products
    for i in range(1, n):
        result[i] = result[i-1] * nums[i-1]
    
    # Right products
    right = 1
    for i in range(n-1, -1, -1):
        result[i] *= right
        right *= nums[i]
    
    return result
```

### Common Pitfalls and How to Avoid Them

1. **Index Management**
   - Use 1-based indexing for prefix arrays to handle edge cases
   - Be careful with range boundaries (inclusive vs exclusive)

2. **Integer Overflow**
   - Consider using appropriate data types for large sums
   - Handle negative numbers correctly

3. **Memory Optimization**
   - For single queries, direct calculation might be better
   - Consider in-place modifications when possible

---
*Master prefix sums to efficiently solve range query and subarray problems!*