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

1. **Identify the pattern** - Look for contiguous subarray/substring problems with optimization opportunities
2. **Choose window type** - Fixed vs variable size based on problem constraints
3. **Track window state efficiently** - Use hashmaps, sets, or counters for frequency tracking
4. **Handle edge cases** - Empty arrays, single elements, window larger than array
5. **Start simple** - Begin with brute force, then optimize with sliding window
6. **Master pointer movement** - Understand when to expand vs shrink the window
7. **Practice common variations** - Max/min window, exactly K vs at most K problems

### Comprehensive Implementation Patterns

**1. Fixed Size Window Templates:**

```python
# Maximum sum of k consecutive elements
def max_sum_subarray_k(arr, k):
    if len(arr) < k:
        return 0
    
    # Calculate sum of first window
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Slide window and update maximum
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

# Average of all subarrays of size k
def find_averages(arr, k):
    if len(arr) < k:
        return []
    
    result = []
    window_sum = sum(arr[:k])
    result.append(window_sum / k)
    
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i-k] + arr[i]
        result.append(window_sum / k)
    
    return result

# Maximum of all subarrays of size k (using deque)
from collections import deque

def max_sliding_window(arr, k):
    if not arr or k == 0:
        return []
    
    dq = deque()  # Store indices
    result = []
    
    for i in range(len(arr)):
        # Remove indices outside current window
        while dq and dq[0] <= i - k:
            dq.popleft()
        
        # Remove indices with smaller values (maintain decreasing order)
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()
        
        dq.append(i)
        
        # Add to result if window is complete
        if i >= k - 1:
            result.append(arr[dq[0]])
    
    return result
```

**2. Variable Size Window Templates:**

```python
# Longest substring with unique characters
def longest_unique_substring(s):
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        # Shrink window until no duplicates
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Longest substring with at most k distinct characters
def longest_substring_k_distinct(s, k):
    if k == 0:
        return 0
    
    char_count = {}
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        
        # Shrink window if more than k distinct characters
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
        
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Minimum window substring containing all characters of pattern
def min_window_substring(s, t):
    if not s or not t or len(s) < len(t):
        return ""
    
    # Count characters in pattern
    pattern_count = {}
    for char in t:
        pattern_count[char] = pattern_count.get(char, 0) + 1
    
    left = 0
    min_len = float('inf')
    min_start = 0
    required = len(pattern_count)
    formed = 0
    window_count = {}
    
    for right in range(len(s)):
        char = s[right]
        window_count[char] = window_count.get(char, 0) + 1
        
        if char in pattern_count and window_count[char] == pattern_count[char]:
            formed += 1
        
        # Try to shrink window
        while left <= right and formed == required:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_start = left
            
            char = s[left]
            window_count[char] -= 1
            if char in pattern_count and window_count[char] < pattern_count[char]:
                formed -= 1
            
            left += 1
    
    return s[min_start:min_start + min_len] if min_len != float('inf') else ""
```

**3. Advanced Sliding Window Patterns:**

```python
# Longest repeating character replacement
def character_replacement(s, k):
    char_count = {}
    left = 0
    max_length = 0
    max_count = 0
    
    for right in range(len(s)):
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        max_count = max(max_count, char_count[s[right]])
        
        # If window size - max frequency > k, shrink window
        if (right - left + 1) - max_count > k:
            char_count[s[left]] -= 1
            left += 1
        
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Permutation in string (sliding window with frequency matching)
def check_inclusion(s1, s2):
    if len(s1) > len(s2):
        return False
    
    s1_count = {}
    for char in s1:
        s1_count[char] = s1_count.get(char, 0) + 1
    
    window_count = {}
    window_size = len(s1)
    
    for i in range(len(s2)):
        # Add character to window
        char = s2[i]
        window_count[char] = window_count.get(char, 0) + 1
        
        # Remove character from window if size exceeds
        if i >= window_size:
            left_char = s2[i - window_size]
            window_count[left_char] -= 1
            if window_count[left_char] == 0:
                del window_count[left_char]
        
        # Check if current window is a permutation
        if window_count == s1_count:
            return True
    
    return False

# Maximum fruits in baskets (at most 2 types)
def total_fruit(fruits):
    fruit_count = {}
    left = 0
    max_fruits = 0
    
    for right in range(len(fruits)):
        fruit_count[fruits[right]] = fruit_count.get(fruits[right], 0) + 1
        
        # More than 2 types of fruits
        while len(fruit_count) > 2:
            fruit_count[fruits[left]] -= 1
            if fruit_count[fruits[left]] == 0:
                del fruit_count[fruits[left]]
            left += 1
        
        max_fruits = max(max_fruits, right - left + 1)
    
    return max_fruits

# Subarray product less than K
def num_subarrays_product_less_than_k(nums, k):
    if k <= 1:
        return 0
    
    left = 0
    product = 1
    count = 0
    
    for right in range(len(nums)):
        product *= nums[right]
        
        while product >= k:
            product //= nums[left]
            left += 1
        
        # All subarrays ending at right and starting from left to right
        count += right - left + 1
    
    return count
```

**4. Multi-Window and Complex Patterns:**

```python
# Sliding window maximum with multiple windows
def sliding_window_maximum_multiple(arr, windows):
    result = {}
    
    for k in windows:
        result[k] = max_sliding_window(arr, k)
    
    return result

# Two sliding windows problem
def max_sum_two_no_overlap(nums, first_len, second_len):
    def max_sum_subarray_ending_at(arr, k):
        # Returns max sum of subarray of length k ending at each position
        result = [0] * len(arr)
        window_sum = sum(arr[:k])
        result[k-1] = window_sum
        
        for i in range(k, len(arr)):
            window_sum = window_sum - arr[i-k] + arr[i]
            result[i] = window_sum
        
        return result
    
    def max_sum_subarray_starting_at(arr, k):
        # Returns max sum of subarray of length k starting at each position
        result = [0] * (len(arr) - k + 1)
        window_sum = sum(arr[:k])
        result[0] = window_sum
        
        for i in range(1, len(result)):
            window_sum = window_sum - arr[i-1] + arr[i+k-1]
            result[i] = window_sum
        
        return result
    
    # Try first array before second array
    max_first_ending = max_sum_subarray_ending_at(nums, first_len)
    max_second_starting = max_sum_subarray_starting_at(nums, second_len)
    
    max_val = 0
    for i in range(first_len - 1, len(nums) - second_len):
        max_val = max(max_val, max_first_ending[i] + max_second_starting[i + 1])
    
    # Try second array before first array
    max_second_ending = max_sum_subarray_ending_at(nums, second_len)
    max_first_starting = max_sum_subarray_starting_at(nums, first_len)
    
    for i in range(second_len - 1, len(nums) - first_len):
        max_val = max(max_val, max_second_ending[i] + max_first_starting[i + 1])
    
    return max_val
```

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

### Problem-Solving Strategy and Decision Tree

**Step-by-Step Approach:**

1. **Identify if sliding window applies:**
   - Problem involves contiguous subarray/substring?
   - Looking for optimal window (max/min length, sum, etc.)?
   - Nested loops can be optimized?

2. **Determine window type:**
   - **Fixed size**: Problem specifies exact window size
   - **Variable size**: Window grows/shrinks based on conditions
   - **Expandable**: Window only grows until condition breaks
   - **Shrinkable**: Window shrinks to maintain condition

3. **Choose data structures:**
   - **HashSet**: For uniqueness constraints
   - **HashMap**: For frequency counting
   - **Deque**: For min/max in sliding window
   - **Variables**: For simple sum/count tracking

**Decision Tree:**
```
Is it a contiguous subarray problem?
├── Yes: Consider sliding window
│   ├── Fixed window size given?
│   │   ├── Yes: Use fixed window template
│   │   └── No: Use variable window template
│   └── Need to track frequency/uniqueness?
│       ├── Yes: Use HashMap/HashSet
│       └── No: Use simple variables
└── No: Consider other patterns
```

### Advanced Optimizations and Techniques

**1. Early Termination:**
```python
def find_substring_early_termination(s, pattern):
    if len(pattern) > len(s):
        return False
    
    # Early termination conditions
    pattern_chars = set(pattern)
    if not all(c in s for c in pattern_chars):
        return False
    
    # Continue with sliding window...
    return sliding_window_logic(s, pattern)
```

**2. Preprocessing Optimizations:**
```python
def optimized_sliding_window(arr, k):
    if len(arr) < k:
        return []
    
    # Precompute prefix sums for O(1) range sum queries
    prefix_sums = [0]
    for num in arr:
        prefix_sums.append(prefix_sums[-1] + num)
    
    result = []
    for i in range(len(arr) - k + 1):
        window_sum = prefix_sums[i + k] - prefix_sums[i]
        result.append(window_sum)
    
    return result
```

**3. Space Optimization:**
```python
def space_optimized_window(s, k):
    # Use rolling hash for string matching
    base = 26
    mod = 10**9 + 7
    
    pattern_hash = 0
    window_hash = 0
    power = pow(base, k - 1, mod)
    
    # Calculate pattern hash and first window hash
    for i in range(k):
        pattern_hash = (pattern_hash * base + ord(pattern[i])) % mod
        window_hash = (window_hash * base + ord(s[i])) % mod
    
    if pattern_hash == window_hash:
        return 0
    
    # Slide the window
    for i in range(k, len(s)):
        # Remove leftmost character, add rightmost character
        window_hash = (window_hash - ord(s[i-k]) * power) % mod
        window_hash = (window_hash * base + ord(s[i])) % mod
        
        if pattern_hash == window_hash:
            return i - k + 1
    
    return -1
```

### Common Pitfalls and Solutions

1. **Window Size Validation**
   - **Problem**: Not checking if array size < window size
   - **Solution**: Always validate input size first
   - **Code**: `if len(arr) < k: return appropriate_default`

2. **Index Management Errors**
   - **Problem**: Off-by-one errors in pointer movement
   - **Solution**: Use clear variable names and test with small examples
   - **Pattern**: `left`, `right` for window boundaries

3. **State Management Issues**
   - **Problem**: Forgetting to update window state when sliding
   - **Solution**: Always update both add and remove operations
   - **Template**: Add new element → Check condition → Remove old elements

4. **Frequency Count Bugs**
   - **Problem**: Not handling zero counts properly
   - **Solution**: Remove keys when count reaches zero
   - **Code**: `if count[key] == 0: del count[key]`

5. **Integer Overflow**
   - **Problem**: Large sums causing overflow
   - **Solution**: Use appropriate data types or modular arithmetic
   - **Check**: Consider maximum possible values

### Performance Analysis and Benchmarking

**Time Complexity Comparison:**

| Problem Type | Brute Force | Sliding Window | Improvement |
|--------------|-------------|----------------|-------------|
| Fixed window sum | O(n*k) | O(n) | k times faster |
| Variable window | O(n²) | O(n) | n times faster |
| Multiple conditions | O(n³) | O(n) | n² times faster |

**Space Complexity:**
- **Fixed window**: O(1) to O(k)
- **Variable window**: O(k) for frequency maps
- **Multiple conditions**: O(alphabet_size) typically

**Benchmark Testing:**
```python
import time
import random

def benchmark_sliding_window():
    sizes = [1000, 10000, 100000]
    window_sizes = [10, 100, 1000]
    
    for n in sizes:
        arr = [random.randint(1, 100) for _ in range(n)]
        
        for k in window_sizes:
            if k > n:
                continue
                
            # Brute force
            start_time = time.time()
            brute_force_max_sum(arr, k)
            brute_time = time.time() - start_time
            
            # Sliding window
            start_time = time.time()
            sliding_window_max_sum(arr, k)
            sliding_time = time.time() - start_time
            
            improvement = brute_time / sliding_time if sliding_time > 0 else float('inf')
            
            print(f"n={n}, k={k}: {improvement:.2f}x improvement")

def brute_force_max_sum(arr, k):
    max_sum = float('-inf')
    for i in range(len(arr) - k + 1):
        current_sum = sum(arr[i:i+k])
        max_sum = max(max_sum, current_sum)
    return max_sum

def sliding_window_max_sum(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum
```

### Testing and Validation Framework

**Test Case Generator:**
```python
def generate_test_cases():
    test_cases = []
    
    # Edge cases
    test_cases.extend([
        ([], 1),  # Empty array
        ([1], 1),  # Single element
        ([1, 2], 3),  # Window larger than array
    ])
    
    # Normal cases
    test_cases.extend([
        ([1, 2, 3, 4, 5], 2),  # Basic case
        ([1, 1, 1, 1, 1], 3),  # All same elements
        ([-1, -2, -3, -4], 2),  # All negative
        ([5, -1, 2, -3, 4], 3),  # Mixed positive/negative
    ])
    
    # Large cases
    import random
    large_array = [random.randint(-100, 100) for _ in range(1000)]
    test_cases.append((large_array, 50))
    
    return test_cases

def validate_sliding_window_function(func):
    test_cases = generate_test_cases()
    
    for i, (arr, k) in enumerate(test_cases):
        try:
            result = func(arr, k)
            print(f"Test {i}: {'PASS' if result is not None else 'FAIL'}")
        except Exception as e:
            print(f"Test {i}: ERROR - {e}")
```

---
*Master the sliding window technique to efficiently solve array and string optimization problems!*