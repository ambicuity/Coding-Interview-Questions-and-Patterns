# Pair Sum - Unsorted

**Author:** Ritesh Rana

## Problem Statement

Given an array of integers `nums` and an integer `target`, return the **indices** of the two numbers such that they add up to `target`. You may assume that each input would have **exactly one solution**, and you may not use the same element twice.

You can return the answer in any order.

### Examples

**Example 1:**
- **Input:** `nums = [2,7,11,15]`, `target = 9`
- **Output:** `[0,1]`
- **Explanation:** Because `nums[0] + nums[1] = 2 + 7 = 9`, we return `[0, 1]`.

**Example 2:**
- **Input:** `nums = [3,2,4]`, `target = 6`
- **Output:** `[1,2]`
- **Explanation:** Because `nums[1] + nums[2] = 2 + 4 = 6`, we return `[1, 2]`.

**Example 3:**
- **Input:** `nums = [3,3]`, `target = 6`
- **Output:** `[0,1]`
- **Explanation:** Because `nums[0] + nums[1] = 3 + 3 = 6`, we return `[0, 1]`.

## Intuition

This is the classic **Two Sum** problem - one of the most important problems to understand in coding interviews. The key insight is to use a hash map to store numbers we've seen along with their indices, allowing us to find the complement in constant time.

For each number in the array, we ask: **"What number do I need to add to the current number to get the target?"**

This complement is simply: `complement = target - current_number`

If we've seen this complement before, we found our answer!

## Algorithm Approaches

### Approach 1: Hash Map (Optimal)

The most efficient approach uses a hash map to store numbers we've seen and their indices.

**Steps:**
1. Create a hash map to store `{number: index}` pairs
2. For each element, calculate its complement: `complement = target - current_number`
3. Check if complement exists in the hash map
4. If yes, return indices; if no, store current number and continue

### Approach 2: Brute Force (For Learning)

Check every possible pair - useful for understanding the problem.

**Steps:**
1. Use nested loops to check all pairs
2. For each pair `(i, j)` where `i < j`, check if `nums[i] + nums[j] == target`
3. Return indices when found

### Approach 3: Sort + Two Pointers (Alternative)

Sort the array but track original indices - shows different thinking.

**Note:** This changes the original array structure, so it's not ideal for this problem.

## Implementation

### Python Solution

```python
from typing import List, Dict

def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Find two numbers that sum to target using hash map.
    
    Args:
        nums: List of integers
        target: Target sum value
        
    Returns:
        List of two indices whose values sum to target
    """
    seen: Dict[int, int] = {}  # {number: index}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in seen:
            return [seen[complement], i]
        
        seen[num] = i
    
    return []  # No solution found (shouldn't happen per problem constraints)
```

### JavaScript Solution

```javascript
/**
 * Find two numbers that sum to target using hash map.
 * @param {number[]} nums - Array of integers
 * @param {number} target - Target sum value
 * @returns {number[]} Array of two indices
 */
function twoSum(nums, target) {
    const seen = new Map(); // Map<number, index>
    
    for (let i = 0; i < nums.length; i++) {
        const num = nums[i];
        const complement = target - num;
        
        if (seen.has(complement)) {
            return [seen.get(complement), i];
        }
        
        seen.set(num, i);
    }
    
    return []; // No solution found
}

// Alternative using object
function twoSumObject(nums, target) {
    const seen = {}; // {number: index}
    
    for (let i = 0; i < nums.length; i++) {
        const num = nums[i];
        const complement = target - num;
        
        if (complement in seen) {
            return [seen[complement], i];
        }
        
        seen[num] = i;
    }
    
    return [];
}
```

### Java Solution

```java
import java.util.*;

public int[] twoSum(int[] nums, int target) {
    Map<Integer, Integer> seen = new HashMap<>(); // {number: index}
    
    for (int i = 0; i < nums.length; i++) {
        int complement = target - nums[i];
        
        if (seen.containsKey(complement)) {
            return new int[]{seen.get(complement), i};
        }
        
        seen.put(nums[i], i);
    }
    
    return new int[]{}; // No solution found
}
```

## Alternative Implementations

### Brute Force Solution

```python
def two_sum_brute_force(nums: List[int], target: int) -> List[int]:
    """
    Brute force solution for comparison - O(n²) time complexity.
    """
    n = len(nums)
    
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    
    return []
```

### Sort + Two Pointers Solution

```python
def two_sum_sorted(nums: List[int], target: int) -> List[int]:
    """
    Sort + two pointers approach (modifies understanding of indices).
    """
    # Create list of (value, original_index) pairs
    indexed_nums = [(num, i) for i, num in enumerate(nums)]
    indexed_nums.sort()  # Sort by value
    
    left, right = 0, len(indexed_nums) - 1
    
    while left < right:
        current_sum = indexed_nums[left][0] + indexed_nums[right][0]
        
        if current_sum == target:
            # Return original indices
            return sorted([indexed_nums[left][1], indexed_nums[right][1]])
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return []
```

## Complexity Analysis

### Hash Map Solution (Optimal)
- **Time Complexity:** **O(n)** where n is the length of the array. We traverse the array once.
- **Space Complexity:** **O(n)** in the worst case, we store all elements in the hash map.

### Brute Force Solution
- **Time Complexity:** **O(n²)** due to nested loops.
- **Space Complexity:** **O(1)** only using constant extra space.

### Sort + Two Pointers Solution
- **Time Complexity:** **O(n log n)** due to sorting.
- **Space Complexity:** **O(n)** for storing indexed pairs.

## Step-by-Step Example

Let's trace through `nums = [2,7,11,15]`, `target = 9`:

```
Step 1: i=0, num=2
  complement = 9 - 2 = 7
  seen = {} (empty)
  7 not in seen, so add 2: seen = {2: 0}

Step 2: i=1, num=7
  complement = 9 - 7 = 2
  seen = {2: 0}
  2 in seen! Return [seen[2], 1] = [0, 1]
```

## Edge Cases and Test Cases

### Comprehensive Test Suite

```python
def test_two_sum():
    """Test function with various scenarios."""
    test_cases = [
        {
            'nums': [2, 7, 11, 15],
            'target': 9,
            'expected': [0, 1],
            'description': 'Basic example - first two elements'
        },
        {
            'nums': [3, 2, 4],
            'target': 6,
            'expected': [1, 2],
            'description': 'Target is sum of last two elements'
        },
        {
            'nums': [3, 3],
            'target': 6,
            'expected': [0, 1],
            'description': 'Duplicate numbers'
        },
        {
            'nums': [1, 2, 3, 4, 5],
            'target': 8,
            'expected': [2, 4],
            'description': 'Multiple possible pairs - return any valid one'
        },
        {
            'nums': [5, 5, 5, 5],
            'target': 10,
            'expected': [0, 1],
            'description': 'All same numbers'
        },
        {
            'nums': [-1, -2, -3, -4, -5],
            'target': -8,
            'expected': [2, 4],
            'description': 'Negative numbers'
        },
        {
            'nums': [0, 4, 3, 0],
            'target': 0,
            'expected': [0, 3],
            'description': 'Target is zero'
        },
        {
            'nums': [-3, 4, 3, 90],
            'target': 0,
            'expected': [0, 2],
            'description': 'Positive and negative numbers'
        }
    ]
    
    for i, test in enumerate(test_cases, 1):
        result = two_sum(test['nums'], test['target'])
        brute_result = two_sum_brute_force(test['nums'], test['target'])
        
        # Verify that the result is correct (indices might vary for multiple solutions)
        if result:
            actual_sum = test['nums'][result[0]] + test['nums'][result[1]]
            success = actual_sum == test['target'] and result[0] != result[1]
        else:
            success = False
            
        status = "✓ PASS" if success else "✗ FAIL"
        
        print(f"Test {i}: {test['description']}")
        print(f"Input: nums = {test['nums']}, target = {test['target']}")
        print(f"Hash Map: {result}")
        print(f"Brute Force: {brute_result}")
        if result:
            print(f"Verification: {test['nums'][result[0]]} + {test['nums'][result[1]]} = {actual_sum}")
        print(f"Result: {status}")
        print("-" * 50)
```

### Edge Cases to Consider

| Input | Target | Expected | Description |
|-------|--------|----------|-------------|
| `[1,2]` | `3` | `[0,1]` | Minimum input size |
| `[3,3]` | `6` | `[0,1]` | Duplicate elements |
| `[-1,-1]` | `-2` | `[0,1]` | Negative duplicates |
| `[0,1]` | `1` | `[0,1]` | One element is zero |
| `[2,5,5,11]` | `10` | `[1,2]` | Multiple same values |

## Interview Tips for Two Sum

💡 **Key Points to Remember:**

1. **Start with hash map approach** - It's the optimal solution
2. **Explain the complement concept** - This shows your thinking process
3. **Handle the duplicate case** - What if the same number appears twice?
4. **Discuss trade-offs** - Time vs space complexity
5. **Consider follow-up questions** - What if multiple solutions exist?
6. **Code defensively** - Handle edge cases and invalid inputs

### Common Follow-up Questions

1. **"What if multiple solutions exist?"** - Return all pairs, return any valid pair
2. **"What if no solution exists?"** - Return empty array, return -1, throw exception
3. **"What if the array is sorted?"** - Two pointers approach might be better
4. **"What about Three Sum?"** - Extends to fixing one element and finding two sum
5. **"What if we can't use extra space?"** - Brute force or sort + two pointers

### Implementation Variations

```python
# Return all valid pairs (if multiple solutions exist)
def two_sum_all_pairs(nums: List[int], target: int) -> List[List[int]]:
    """Find all pairs that sum to target."""
    seen = {}
    pairs = []
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in seen:
            # Found a pair - add all combinations
            for prev_index in seen[complement]:
                pairs.append([prev_index, i])
        
        # Store this number and its index
        if num not in seen:
            seen[num] = []
        seen[num].append(i)
    
    return pairs

# Using Counter for frequency-based approach
from collections import Counter

def two_sum_counter(nums: List[int], target: int) -> List[int]:
    """Alternative using Counter for educational purposes."""
    counter = Counter(nums)
    num_to_index = {}
    
    for i, num in enumerate(nums):
        if num not in num_to_index:
            num_to_index[num] = i
        else:
            # Handle duplicates by storing later index
            pass
    
    for num in counter:
        complement = target - num
        
        if complement in counter:
            if complement == num and counter[num] >= 2:
                # Same number used twice
                indices = [i for i, x in enumerate(nums) if x == num]
                return indices[:2]
            elif complement != num:
                return [num_to_index[num], num_to_index[complement]]
    
    return []
```

## Related Problems

- **3Sum** - Find three numbers that sum to target
- **4Sum** - Find four numbers that sum to target
- **Two Sum II - Input array is sorted** - Use two pointers
- **Two Sum III - Data structure design** - Design add/find operations
- **Valid Two Sum Tree** - Two sum in binary search tree
- **Two Sum Less Than K** - Find pair with sum less than K

## Common Mistakes to Avoid

❌ **Don't use nested loops as first solution** - Always think hash map first
❌ **Don't forget about the same element twice** - `nums[i]` can't be used twice
❌ **Don't assume array is sorted** - Hash map works for unsorted arrays
❌ **Don't return the values** - Problem asks for indices
❌ **Don't modify the input array** - Preserve original structure
❌ **Don't over-complicate edge cases** - Problem guarantees exactly one solution

✅ **Do explain your thinking process** - Show the complement concept
✅ **Do handle the hash map correctly** - Store after checking, not before
✅ **Do consider multiple approaches** - Show you understand trade-offs
✅ **Do trace through an example** - Demonstrates understanding
✅ **Do discuss complexity** - Time and space trade-offs

---
*Two Sum is the foundation of many array problems - master this pattern and you'll solve many more!*