# Two Pointers Pattern

**Author:** Ritesh Rana

## Introduction to Two Pointers

The Two Pointers technique is a fundamental algorithmic pattern that uses two pointers to traverse data structures (typically arrays or strings) to solve problems efficiently. This approach is particularly powerful when dealing with sorted arrays, searching for pairs, or when you need to process elements from both ends of a structure simultaneously.

### Key Concepts

**Core Principles:**
- **Pointer Placement**: Strategic positioning of two pointers based on problem requirements
- **Movement Strategy**: Conditional movement of pointers to explore the solution space efficiently
- **State Tracking**: Maintaining relevant information as pointers move
- **Termination Conditions**: Clear criteria for when to stop the algorithm

**Pointer Movement Patterns:**
1. **Converging**: Pointers start from opposite ends and move toward each other
2. **Expanding**: Pointers start from center and move outward
3. **Sliding**: Both pointers move in the same direction at different speeds
4. **Fixed-Distance**: Maintain constant distance between pointers

### Common Patterns and Applications

1. **Target Sum Problems** - Finding pairs/triplets that sum to target
2. **Palindrome Verification** - Checking if string/array is palindromic
3. **Container Problems** - Maximizing area/volume calculations  
4. **Array Partitioning** - Segregating elements based on conditions
5. **Duplicate Removal** - Eliminating duplicates in sorted arrays
6. **Subarray Problems** - Finding subarrays with specific properties
7. **String Manipulation** - Reversing, matching patterns

### When to Use Two Pointers

**Ideal Scenarios:**
- Working with sorted arrays or strings
- Need to find pairs/triplets with specific sum
- Palindrome-related problems
- Container/area maximization problems
- Array partitioning and rearrangement
- Merging sorted sequences
- Problems that can reduce O(n²) brute force to O(n)

**Problem Identification Signals:**
- Keywords: "pair", "triplet", "two elements", "palindrome", "container"
- Sorted input (or can be sorted)
- Need to compare elements from different positions
- Can eliminate nested loops with smart pointer movement

### Comprehensive Implementation Templates

**1. Converging Two Pointers (Opposite Direction):**
```python
def two_pointer_converging_template(arr, target):
    """Template for problems where pointers start from opposite ends"""
    left, right = 0, len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return [left, right]  # Found solution
        elif current_sum < target:
            left += 1  # Need larger sum
        else:
            right -= 1  # Need smaller sum
    
    return None  # No solution found

# Example: Two Sum in Sorted Array
def two_sum_sorted(numbers, target):
    """Find two numbers that add up to target in sorted array"""
    left, right = 0, len(numbers) - 1
    
    while left < right:
        current_sum = numbers[left] + numbers[right]
        
        if current_sum == target:
            return [left + 1, right + 1]  # 1-indexed result
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return []

# Example: Container With Most Water
def max_area(heights):
    """Find maximum water container area"""
    left, right = 0, len(heights) - 1
    max_water = 0
    
    while left < right:
        # Calculate current area
        width = right - left
        height = min(heights[left], heights[right])
        current_area = width * height
        max_water = max(max_water, current_area)
        
        # Move pointer with smaller height
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    
    return max_water
```

**2. Same Direction Two Pointers (Sliding Window Style):**
```python
def two_pointer_same_direction_template(arr):
    """Template where both pointers move in same direction"""
    slow = fast = 0
    
    while fast < len(arr):
        # Process current element at fast pointer
        
        # Move fast pointer
        fast += 1
        
        # Move slow pointer based on condition
        if condition_met():
            slow += 1
    
    return result

# Example: Remove Duplicates from Sorted Array
def remove_duplicates(nums):
    """Remove duplicates in-place, return new length"""
    if not nums:
        return 0
    
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    
    return slow + 1

# Example: Move Zeros to End
def move_zeros(nums):
    """Move all zeros to end while maintaining relative order"""
    slow = 0
    
    # First pass: move all non-zero elements to front
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow] = nums[fast]
            slow += 1
    
    # Second pass: fill remaining with zeros
    while slow < len(nums):
        nums[slow] = 0
        slow += 1
    
    return nums

# Alternative: Swap-based approach
def move_zeros_swap(nums):
    """Move zeros using swap approach"""
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
    
    return nums
```

**3. Palindrome Pattern:**
```python
def palindrome_template(s):
    """Template for palindrome checking"""
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True

# Example: Valid Palindrome (alphanumeric only)
def is_palindrome(s):
    """Check if string is palindrome, considering only alphanumeric"""
    left, right = 0, len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric characters
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        
        # Compare characters (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True

# Example: Longest Palindromic Substring (expand around centers)
def longest_palindrome(s):
    """Find longest palindromic substring"""
    if not s:
        return ""
    
    start = 0
    max_len = 1
    
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
    
    for i in range(len(s)):
        # Check for odd-length palindromes
        len1 = expand_around_center(i, i)
        # Check for even-length palindromes
        len2 = expand_around_center(i, i + 1)
        
        current_max = max(len1, len2)
        if current_max > max_len:
            max_len = current_max
            start = i - (current_max - 1) // 2
    
    return s[start:start + max_len]
```

**4. Three Sum and Multi-Pointer Extensions:**
```python
def three_sum(nums):
    """Find all unique triplets that sum to zero"""
    nums.sort()
    result = []
    
    for i in range(len(nums) - 2):
        # Skip duplicates for first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        # Use two pointers for remaining elements
        left, right = i + 1, len(nums) - 1
        target = -nums[i]
        
        while left < right:
            current_sum = nums[left] + nums[right]
            
            if current_sum == target:
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    
    return result

def four_sum(nums, target):
    """Find all unique quadruplets that sum to target"""
    nums.sort()
    result = []
    n = len(nums)
    
    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            
            left, right = j + 1, n - 1
            two_sum_target = target - nums[i] - nums[j]
            
            while left < right:
                current_sum = nums[left] + nums[right]
                
                if current_sum == two_sum_target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif current_sum < two_sum_target:
                    left += 1
                else:
                    right -= 1
    
    return result
```

**5. Advanced Two Pointer Techniques:**
```python
def partition_array(nums, pivot):
    """Partition array around pivot (Dutch National Flag style)"""
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        if nums[left] < pivot:
            left += 1
        elif nums[right] > pivot:
            right -= 1
        else:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    
    return nums

def sort_colors(nums):
    """Sort array with 0s, 1s, 2s (Dutch National Flag)"""
    red, white, blue = 0, 0, len(nums) - 1
    
    while white <= blue:
        if nums[white] == 0:
            nums[red], nums[white] = nums[white], nums[red]
            red += 1
            white += 1
        elif nums[white] == 1:
            white += 1
        else:  # nums[white] == 2
            nums[white], nums[blue] = nums[blue], nums[white]
            blue -= 1
            # Don't increment white here, need to check swapped element
    
    return nums

def trapping_rain_water(height):
    """Calculate trapped rainwater using two pointers"""
    if not height:
        return 0
    
    left, right = 0, len(height) - 1
    left_max = right_max = 0
    water = 0
    
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    
    return water
```

## Interview Tips for Two Pointers

💡 **Key Interview Tips:**

1. **Identify the pattern early** - Look for sorted arrays, pairs/triplets, palindromes, or container problems
2. **Ask about array properties** - Is it sorted? Can it be sorted? Are there duplicates?
3. **Choose the right pointer movement** - Converging, expanding, or same-direction sliding
4. **Handle edge cases systematically** - Empty arrays, single elements, all duplicates
5. **Watch for infinite loops** - Ensure pointers always make progress toward termination
6. **Consider multiple passes** - Fix one element, then use two pointers on the rest
7. **Master duplicate handling** - Skip duplicates to avoid redundant solutions
8. **Think about invariants** - What properties are maintained as pointers move?

### Problem-Solving Strategy Guide

**Step-by-Step Approach:**

1. **Identify if two pointers applies:**
   - Can brute force O(n²) be optimized?
   - Are we looking for pairs/relationships between elements?
   - Is there a sorted property we can exploit?

2. **Choose pointer initialization:**
   - **Opposite ends**: Sum problems, palindromes, containers
   - **Same start**: Remove duplicates, partitioning
   - **Center expansion**: Palindrome substring problems

3. **Define movement rules:**
   - When to move left pointer?
   - When to move right pointer?
   - When to move both?

4. **Handle termination and edge cases:**
   - What happens when pointers meet/cross?
   - Empty input, single element cases
   - All elements same, no solution exists

**Decision Tree:**
```
Is the array sorted (or can be sorted)?
├── Yes: Consider two pointers
│   ├── Looking for target sum → Converging pointers
│   ├── Checking palindrome → Converging from ends
│   ├── Container/area problem → Converging pointers
│   ├── Remove duplicates → Same direction pointers
│   └── Partitioning → Dutch flag approach
└── No: Consider if problem has other patterns or if sorting helps
```

### Advanced Techniques and Optimizations

**1. Skip Duplicates Pattern:**
```python
def skip_duplicates_template(nums):
    """Template for handling duplicates in sorted array"""
    # After processing element at index i
    while i < len(nums) - 1 and nums[i] == nums[i + 1]:
        i += 1  # Skip duplicate elements
    
    return i

# Example in Three Sum context
def three_sum_optimized(nums):
    nums.sort()
    result = []
    
    for i in range(len(nums) - 2):
        # Skip duplicate first elements
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates for second element
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # Skip duplicates for third element
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    
    return result
```

**2. Multiple Conditions Handling:**
```python
def two_pointers_multiple_conditions(nums, condition1, condition2):
    """Handle multiple conditions with priority"""
    left, right = 0, len(nums) - 1
    
    while left < right:
        if condition1(nums[left], nums[right]):
            # Handle primary condition
            process_condition1()
        elif condition2(nums[left], nums[right]):
            # Handle secondary condition
            process_condition2()
        else:
            # Default movement strategy
            default_movement()
    
    return result

# Example: Find closest sum to target
def three_sum_closest(nums, target):
    nums.sort()
    closest_sum = float('inf')
    
    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            # Update closest sum if current is closer to target
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum
            
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                return current_sum  # Exact match found
    
    return closest_sum
```

**3. Dynamic Pointer Adjustment:**
```python
def squares_of_sorted_array(nums):
    """Square sorted array with negative numbers"""
    left, right = 0, len(nums) - 1
    result = [0] * len(nums)
    pos = len(nums) - 1
    
    while left <= right:
        left_square = nums[left] ** 2
        right_square = nums[right] ** 2
        
        if left_square > right_square:
            result[pos] = left_square
            left += 1
        else:
            result[pos] = right_square
            right -= 1
        
        pos -= 1
    
    return result

def merge_sorted_arrays(nums1, m, nums2, n):
    """Merge two sorted arrays in-place"""
    # Start from the end to avoid overwriting
    p1, p2, p = m - 1, n - 1, m + n - 1
    
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
    
    # Copy remaining elements from nums2
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1
    
    return nums1
```

### Common Pitfalls and Expert Solutions

1. **Infinite Loop Prevention:**
   ```python
   # ❌ Wrong: Pointers might not make progress
   while left < right:
       if condition:
           # Forgot to move pointers!
           pass
   
   # ✅ Correct: Always ensure progress
   while left < right:
       if condition:
           process_result()
           left += 1
           right -= 1
       elif other_condition:
           left += 1
       else:
           right -= 1
   ```

2. **Boundary Condition Errors:**
   ```python
   # ❌ Wrong: May go out of bounds
   while left <= right:  # Should be < for most cases
       # ...
   
   # ✅ Correct: Proper boundary handling
   while left < right:
       # Safe access to nums[left] and nums[right]
       # ...
   ```

3. **Duplicate Handling Mistakes:**
   ```python
   # ❌ Wrong: Incomplete duplicate skipping
   if nums[left] == nums[right]:
       left += 1  # Only moving one pointer
   
   # ✅ Correct: Comprehensive duplicate handling
   if nums[left] == nums[right]:
       # Skip all duplicates on both sides
       val = nums[left]
       while left < right and nums[left] == val:
           left += 1
       while left < right and nums[right] == val:
           right -= 1
   ```

### Performance Analysis and Benchmarking

**Time Complexity Analysis:**
- **Standard Two Pointers**: O(n)
- **With Sorting**: O(n log n) + O(n) = O(n log n)
- **Three Sum**: O(n²) (n iterations × O(n) two-pointer scan)
- **Four Sum**: O(n³) (n² iterations × O(n) two-pointer scan)

**Space Complexity:**
- **In-place algorithms**: O(1)
- **With result storage**: O(k) where k is number of solutions
- **With sorting**: O(log n) for sort, O(1) for two-pointer logic

**Optimization Strategies:**
```python
def optimized_two_sum(nums, target):
    """Optimized with early termination"""
    nums.sort()
    left, right = 0, len(nums) - 1
    
    # Early termination checks
    if nums[left] + nums[left + 1] > target:
        return []  # Minimum possible sum too large
    if nums[right] + nums[right - 1] < target:
        return []  # Maximum possible sum too small
    
    while left < right:
        current_sum = nums[left] + nums[right]
        
        if current_sum == target:
            return [nums[left], nums[right]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return []
```

### Testing and Validation Framework

**Comprehensive Test Suite:**
```python
def test_two_pointers():
    """Test suite for two-pointer algorithms"""
    
    test_cases = [
        # Two Sum tests
        ([2, 7, 11, 15], 9, [0, 1], "Basic two sum"),
        ([2, 3, 4], 6, [0, 2], "Two sum variant"),
        ([-1, 0], -1, [0, 1], "With negative numbers"),
        
        # Three Sum tests
        ([-1, 0, 1, 2, -1, -4], 0, [[-1, -1, 2], [-1, 0, 1]], "Three sum basic"),
        ([0, 1, 1], 0, [], "Three sum no solution"),
        ([0, 0, 0], 0, [[0, 0, 0]], "Three sum all zeros"),
        
        # Container tests
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], None, 49, "Container with most water"),
        ([1, 1], None, 1, "Container minimum case"),
        
        # Palindrome tests
        ("A man a plan a canal Panama", None, True, "Complex palindrome"),
        ("race a car", None, False, "Non-palindrome"),
    ]
    
    algorithms = {
        "two_sum": two_sum_sorted,
        "three_sum": three_sum,
        "container": max_area,
        "palindrome": is_palindrome
    }
    
    for test_input, target, expected, description in test_cases:
        # Choose appropriate algorithm based on test type
        if "two sum" in description.lower():
            result = algorithms["two_sum"](test_input, target)
        elif "three sum" in description.lower():
            result = algorithms["three_sum"](test_input)
        elif "container" in description.lower():
            result = algorithms["container"](test_input)
        elif "palindrome" in description.lower():
            result = algorithms["palindrome"](test_input)
        
        status = "PASS" if validate_result(result, expected) else "FAIL"
        print(f"{description}: {status}")

def validate_result(actual, expected):
    """Validate test results handling different data types"""
    if isinstance(expected, list) and isinstance(actual, list):
        return sorted(actual) == sorted(expected)
    return actual == expected
```

## Problems Covered

1. [Pair Sum - Sorted](./pair-sum-sorted.md) ⭐ (Foundation Problem)
2. [Triplet Sum](./triplet-sum.md) ⭐ (Detailed Example)
3. [Valid Palindrome](./valid-palindrome.md) ⭐ (Complete Implementation)
4. [Container With Most Water](./container-with-most-water.md) ⭐ (Complete Implementation)
5. [Shift Zeros to the End](./shift-zeros-to-end.md)
6. [Next Lexicographical Sequence](./next-lexicographical-sequence.md)

---
*Master the two pointers technique to solve array and string problems efficiently with O(n) time complexity!*