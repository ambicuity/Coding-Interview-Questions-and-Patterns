# Pair Sum - Sorted

**Author:** Ritesh Rana

## Problem Statement

Given a sorted array of integers and a target sum, find two numbers in the array that add up to the target sum. Return the indices of these two numbers (1-indexed). You may assume that each input has exactly one solution, and you cannot use the same element twice.

### Example

**Input:** `nums = [2, 7, 11, 15]`, `target = 9`
**Output:** `[1, 2]`
**Explanation:** `nums[0] + nums[1] = 2 + 7 = 9`, so return indices `[1, 2]` (1-indexed)

## Intuition

Since the array is sorted, we can use the two-pointer technique to solve this problem efficiently. The key insight is that if the current sum is:
- **Less than target**: We need a larger sum, so move the left pointer right
- **Greater than target**: We need a smaller sum, so move the right pointer left
- **Equal to target**: We found our answer!

This approach is much more efficient than the brute force O(n²) solution.

## Algorithm Steps

1. **Initialize two pointers**: Left pointer at start (0), right pointer at end (n-1)
2. **Calculate sum**: Add values at both pointer positions
3. **Compare and move**:
   - If sum equals target: return the indices
   - If sum is less than target: move left pointer right
   - If sum is greater than target: move right pointer left
4. **Repeat** until solution is found

## Implementation

### Python Solution

```python
from typing import List, Optional

def pair_sum_sorted(nums: List[int], target: int) -> Optional[List[int]]:
    """
    Find two numbers in sorted array that sum to target.
    
    Args:
        nums: Sorted list of integers
        target: Target sum value
        
    Returns:
        1-indexed positions of the two numbers, or None if not found
    """
    left, right = 0, len(nums) - 1
    
    while left < right:
        current_sum = nums[left] + nums[right]
        
        if current_sum == target:
            return [left + 1, right + 1]  # Convert to 1-indexed
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return None  # No solution found
```

### JavaScript Solution

```javascript
/**
 * Find two numbers in sorted array that sum to target.
 * @param {number[]} nums - Sorted array of integers
 * @param {number} target - Target sum value
 * @returns {number[]|null} 1-indexed positions or null if not found
 */
function pairSumSorted(nums, target) {
    let left = 0, right = nums.length - 1;
    
    while (left < right) {
        const sum = nums[left] + nums[right];
        
        if (sum === target) {
            return [left + 1, right + 1]; // Convert to 1-indexed
        } else if (sum < target) {
            left++;
        } else {
            right--;
        }
    }
    
    return null; // No solution found
}
```

### Java Solution

```java
public int[] pairSumSorted(int[] nums, int target) {
    int left = 0, right = nums.length - 1;
    
    while (left < right) {
        int sum = nums[left] + nums[right];
        
        if (sum == target) {
            return new int[]{left + 1, right + 1}; // Convert to 1-indexed
        } else if (sum < target) {
            left++;
        } else {
            right--;
        }
    }
    
    return new int[]{}; // No solution found
}
```

## Complexity Analysis

### Time Complexity
**O(n)** where n is the length of the array. In the worst case, we traverse the array once with both pointers.

### Space Complexity
**O(1)** - We only use constant extra space for the two pointers and variables.

## Variations and Follow-ups

### 1. Return All Pairs
If multiple pairs sum to the target:

```python
def pair_sum_sorted_all_pairs(nums: List[int], target: int) -> List[List[int]]:
    """Find all pairs that sum to target."""
    pairs = []
    left, right = 0, len(nums) - 1
    
    while left < right:
        current_sum = nums[left] + nums[right]
        
        if current_sum == target:
            pairs.append([left + 1, right + 1])
            left += 1
            right -= 1
            
            # Skip duplicates
            while left < right and nums[left] == nums[left - 1]:
                left += 1
            while left < right and nums[right] == nums[right + 1]:
                right -= 1
                
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return pairs
```

### 2. Return Values Instead of Indices

```python
def pair_sum_sorted_values(nums: List[int], target: int) -> Optional[List[int]]:
    """Return the actual values instead of indices."""
    left, right = 0, len(nums) - 1
    
    while left < right:
        current_sum = nums[left] + nums[right]
        
        if current_sum == target:
            return [nums[left], nums[right]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return None
```

## Test Cases

### Comprehensive Test Suite

```python
def test_pair_sum_sorted():
    """Test function with various scenarios."""
    test_cases = [
        {
            'nums': [2, 7, 11, 15],
            'target': 9,
            'expected': [1, 2],
            'description': 'Basic example'
        },
        {
            'nums': [2, 3, 4],
            'target': 6,
            'expected': [1, 3],
            'description': 'First and last elements'
        },
        {
            'nums': [-1, 0],
            'target': -1,
            'expected': [1, 2],
            'description': 'Negative numbers'
        },
        {
            'nums': [1, 2, 3, 4, 5],
            'target': 8,
            'expected': [3, 5],
            'description': 'Multiple valid pairs - should find one'
        },
        {
            'nums': [1, 2],
            'target': 5,
            'expected': None,
            'description': 'No solution exists'
        }
    ]
    
    for i, test in enumerate(test_cases, 1):
        result = pair_sum_sorted(test['nums'], test['target'])
        success = result == test['expected']
        status = "✓ PASS" if success else "✗ FAIL"
        
        print(f"Test {i}: {test['description']}")
        print(f"Input: nums = {test['nums']}, target = {test['target']}")
        print(f"Expected: {test['expected']}")
        print(f"Got: {result}")
        print(f"Result: {status}")
        print("-" * 40)
```

### Edge Cases to Consider

| Input | Target | Expected | Description |
|-------|--------|----------|-------------|
| `[1, 2]` | `3` | `[1, 2]` | Minimum array size |
| `[-3, -1, 0, 2]` | `-1` | `[2, 4]` | Mixed positive/negative |
| `[1, 1, 1, 1]` | `2` | `[1, 4]` | All same elements |
| `[1, 5]` | `10` | `None` | No solution |

## Interview Tips for Pair Sum

💡 **Key Points to Remember:**

1. **Confirm array is sorted** - This is crucial for the two-pointer approach
2. **Clarify return format** - Indices vs values, 0-indexed vs 1-indexed
3. **Handle edge cases** - Empty array, no solution, duplicate values
4. **Consider follow-ups** - All pairs, unsorted array (use hash map)
5. **Explain the intuition** - Why moving pointers works with sorted arrays

### Common Follow-up Questions

1. **"What if the array is not sorted?"** - Use hash map approach O(n) time, O(n) space
2. **"What if there are multiple solutions?"** - Return all pairs or specify which one
3. **"What if no solution exists?"** - Return empty array, null, or throw exception
4. **"Can you do this in-place?"** - Yes, two pointers use O(1) space

### Implementation Variations

```python
# Hash map approach for unsorted arrays
def pair_sum_unsorted(nums: List[int], target: int) -> Optional[List[int]]:
    """Find pair sum in unsorted array using hash map."""
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement] + 1, i + 1]  # 1-indexed
        seen[num] = i
    
    return None
```

## Related Problems

- **3Sum (Triplet Sum)** - Extends this concept to three numbers
- **4Sum** - Find four numbers that sum to target
- **Two Sum Closest** - Find pair with sum closest to target
- **Container With Most Water** - Uses similar two-pointer technique

---
*Master the two-pointer technique with sorted arrays - it's a fundamental pattern in many problems!*