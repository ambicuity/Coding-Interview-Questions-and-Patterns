# Triplet Sum

**Author:** Ritesh Rana

## Problem Statement

Given an array of integers, return all triplets `[a, b, c]` such that `a + b + c = 0`. The solution must not contain duplicate triplets (e.g., `[1, 2, 3]` and `[2, 3, 1]` are considered duplicates). If no such triplets are found, return an empty array.

Each triplet can be arranged in any order, and the output can be returned in any order.

### Example

**Input:** `nums = [0, -1, 2, -3, 1]`
**Output:** `[[-3, 1, 2], [-1, 0, 1]]`

## Intuition

A brute force solution involves checking every possible triplet in the array to see if they sum to zero. This can be done using three nested loops, iterating through each combination of three elements.

Duplicate triplets can be avoided by sorting each triplet, which ensures that identical triplets with different representations (e.g., `[1, 3, 2]` and `[3, 2, 1]`) are ordered consistently (e.g., `[1, 2, 3]`). Once sorted, we can add these triplets to a hash set. This way, if the same triplet is encountered again, the hash set will only keep one instance. Below is the code snippet for this approach:

### Brute Force Approach

```python
from typing import List
   
def triplet_sum_brute_force(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    # Use a hash set to ensure we don't add duplicate triplets.
    triplets = set()
    # Iterate through the indexes of all triplets.
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    # Sort the triplet before including it in the hash set.
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                    triplets.add(triplet)
    return [list(triplet) for triplet in triplets]
```

This solution is quite inefficient with a time complexity of **O(n³)**, where **n** denotes the length of the input array. How can we do better?

## Optimized Two-Pointer Solution

Let's see if we can find at least one triplet that sums to 0. Notice that if we fix one of the numbers in a triplet, the problem can be reduced to finding the other two. This leads to the following observation:

**For any triplet [a, b, c], if we fix 'a', we can focus on finding a pair [b, c] that sums to '-a' (a + b + c = 0 → b + c = -a).**

Sound familiar? That's because the problem of finding a pair of numbers that sum to a target has already been addressed by Pair Sum - Sorted. However, we can only use that algorithm on a sorted array. So, the first thing we should do is sort the input.

### Algorithm Steps

1. **Sort the array** to enable two-pointer technique
2. **Fix the first element** (a) and use two pointers for the remaining array
3. **Find pairs** that sum to -a using the two-pointer technique
4. **Handle duplicates** by skipping repeated values

### Handling Duplicate Triplets

There are two cases where duplicates may occur:

#### Case 1: Duplicate 'a' values
The first instance where duplicates may occur is when seeking pairs for triplets that start with the same 'a' value. Since `pair_sum_sorted` would look for pairs that sum to '-a' in both instances, we'd naturally end up with the same pairs and, hence, the same triplets.

To avoid picking the same 'a' value, we keep increasing i (where `nums[i]` represents the value 'a') until it reaches a different number from the previous one.

```python
# To prevent duplicate triplets, ensure 'a' is not a repeat of the previous element
# in the sorted array.
if i > 0 and nums[i] == nums[i - 1]:
    continue
```

#### Case 2: Duplicate 'b' values
For a fixed target value ('-a'), pairs that start with the same number 'b' will always be the same. The remedy is the same: ensure the current 'b' value isn't the same as the previous value.

**Note:** We don't need to explicitly handle duplicate 'c' values. The adjustments made to avoid duplicate 'a' and 'b' values ensure each pair [a, b] is unique. Since 'c' is determined by the equation c = -(a + b), each unique [a, b] pair will result in a unique 'c' value.

### Optimization

An interesting observation is that triplets that sum to 0 cannot be formed using positive numbers alone. Therefore, we can stop trying to find triplets once we reach a positive 'a' value since this implies that 'b' and 'c' would also be positive.

## Implementation

### Python Solution

```python
from typing import List
  
def triplet_sum(nums: List[int]) -> List[List[int]]:
    triplets = []
    nums.sort()
    
    for i in range(len(nums)):
        # Optimization: triplets consisting of only positive numbers will never sum to 0
        if nums[i] > 0:
            break
            
        # To avoid duplicate triplets, skip 'a' if it's the same as the previous number
        if i > 0 and nums[i] == nums[i - 1]:
            continue
            
        # Find all pairs that sum to a target of '-a' ('-nums[i]')
        pairs = pair_sum_sorted_all_pairs(nums, i + 1, -nums[i])
        for pair in pairs:
            triplets.append([nums[i]] + pair)
    
    return triplets
  
def pair_sum_sorted_all_pairs(nums: List[int], start: int, target: int) -> List[List[int]]:
    pairs = []
    left, right = start, len(nums) - 1
    
    while left < right:
        current_sum = nums[left] + nums[right]
        
        if current_sum == target:
            pairs.append([nums[left], nums[right]])
            left += 1
            
            # To avoid duplicate '[b, c]' pairs, skip 'b' if it's the same as the previous number
            while left < right and nums[left] == nums[left - 1]:
                left += 1
                
        elif current_sum < target:
            left += 1 
        else:
            right -= 1
            
    return pairs
```

### JavaScript Solution

```javascript
function tripletSum(nums) {
    const triplets = [];
    nums.sort((a, b) => a - b);
    
    for (let i = 0; i < nums.length; i++) {
        // Optimization: triplets consisting of only positive numbers will never sum to 0
        if (nums[i] > 0) break;
        
        // To avoid duplicate triplets, skip 'a' if it's the same as the previous number
        if (i > 0 && nums[i] === nums[i - 1]) continue;
        
        // Find all pairs that sum to a target of '-a' ('-nums[i]')
        const pairs = pairSumSortedAllPairs(nums, i + 1, -nums[i]);
        for (const pair of pairs) {
            triplets.push([nums[i], ...pair]);
        }
    }
    
    return triplets;
}

function pairSumSortedAllPairs(nums, start, target) {
    const pairs = [];
    let left = start, right = nums.length - 1;
    
    while (left < right) {
        const sum = nums[left] + nums[right];
        
        if (sum === target) {
            pairs.push([nums[left], nums[right]]);
            left++;
            
            // To avoid duplicate '[b, c]' pairs, skip 'b' if it's the same as the previous number
            while (left < right && nums[left] === nums[left - 1]) {
                left++;
            }
        } else if (sum < target) {
            left++;
        } else {
            right--;
        }
    }
    
    return pairs;
}
```

### Java Solution

```java
import java.util.*;

public class TripletSum {
    public List<List<Integer>> tripletSum(int[] nums) {
        List<List<Integer>> triplets = new ArrayList<>();
        Arrays.sort(nums);
        
        for (int i = 0; i < nums.length; i++) {
            // Optimization: triplets consisting of only positive numbers will never sum to 0
            if (nums[i] > 0) break;
            
            // To avoid duplicate triplets, skip 'a' if it's the same as the previous number
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            
            // Find all pairs that sum to a target of '-a' ('-nums[i]')
            List<List<Integer>> pairs = pairSumSortedAllPairs(nums, i + 1, -nums[i]);
            for (List<Integer> pair : pairs) {
                List<Integer> triplet = new ArrayList<>();
                triplet.add(nums[i]);
                triplet.addAll(pair);
                triplets.add(triplet);
            }
        }
        
        return triplets;
    }
    
    private List<List<Integer>> pairSumSortedAllPairs(int[] nums, int start, int target) {
        List<List<Integer>> pairs = new ArrayList<>();
        int left = start, right = nums.length - 1;
        
        while (left < right) {
            int sum = nums[left] + nums[right];
            
            if (sum == target) {
                pairs.add(Arrays.asList(nums[left], nums[right]));
                left++;
                
                // To avoid duplicate '[b, c]' pairs, skip 'b' if it's the same as the previous number
                while (left < right && nums[left] == nums[left - 1]) {
                    left++;
                }
            } else if (sum < target) {
                left++;
            } else {
                right--;
            }
        }
        
        return pairs;
    }
}
```

## Complexity Analysis

### Time Complexity
The time complexity of `triplet_sum` is **O(n²)**. Here's why:

1. We first sort the array, which takes **O(n log(n))** time
2. Then, for each of the **n** elements in the array, we call `pair_sum_sorted_all_pairs` at most once, which runs in **O(n)** time
3. Therefore, the overall time complexity is **O(n log(n)) + O(n²) = O(n²)**

### Space Complexity
The space complexity is **O(n)** due to the space taken up by Python's sorting algorithm. This complexity does not include the output array `triplets` because we're only concerned with the additional space used by the algorithm, not the space needed for the output itself.

If the interviewer asks what the space complexity would be if we included the output array, it would be **O(n²)**. This is because the `pair_sum_sorted_all_pairs` function, in the worst case, can add approximately **n** pairs to the output. Since this function is called approximately **n** times, the overall space complexity is **O(n²)**.

## Test Cases

### Test Your Implementation

```python
def test_triplet_sum():
    # Test case 1: Basic example
    nums1 = [0, -1, 2, -3, 1]
    expected1 = [[-3, 1, 2], [-1, 0, 1]]
    result1 = triplet_sum(nums1)
    print(f"Test 1: {sorted(result1) == sorted(expected1)}")
    
    # Test case 2: Empty array
    nums2 = []
    expected2 = []
    result2 = triplet_sum(nums2)
    print(f"Test 2: {result2 == expected2}")
    
    # Test case 3: Single element array
    nums3 = [0]
    expected3 = []
    result3 = triplet_sum(nums3)
    print(f"Test 3: {result3 == expected3}")
    
    # Test case 4: Two element array
    nums4 = [1, -1]
    expected4 = []
    result4 = triplet_sum(nums4)
    print(f"Test 4: {result4 == expected4}")
    
    # Test case 5: All same values
    nums5 = [0, 0, 0]
    expected5 = [[0, 0, 0]]
    result5 = triplet_sum(nums5)
    print(f"Test 5: {result5 == expected5}")
    
    # Test case 6: No valid triplets
    nums6 = [1, 0, 1]
    expected6 = []
    result6 = triplet_sum(nums6)
    print(f"Test 6: {result6 == expected6}")
    
    # Test case 7: Duplicate triplets
    nums7 = [0, 0, 1, -1, 1, -1]
    expected7 = [[-1, 0, 1]]
    result7 = triplet_sum(nums7)
    print(f"Test 7: {sorted(result7) == sorted(expected7)}")

# Run tests
test_triplet_sum()
```

### Additional Test Cases

| Input | Expected Output | Description |
|-------|----------------|-------------|
| `nums = []` | `[]` | Tests an empty array |
| `nums = [0]` | `[]` | Tests a single-element array |
| `nums = [1, -1]` | `[]` | Tests a two-element array |
| `nums = [0, 0, 0]` | `[[0, 0, 0]]` | Tests an array where all three values are the same |
| `nums = [1, 0, 1]` | `[]` | Tests an array with no triplets that sum to 0 |
| `nums = [0, 0, 1, -1, 1, -1]` | `[[-1, 0, 1]]` | Tests an array with duplicate triplets |

## Interview Tips for Triplet Sum

💡 **Key Points to Remember:**

1. **Always sort first** - This enables the two-pointer technique
2. **Handle duplicates carefully** - Skip duplicate 'a' values and duplicate 'b' values
3. **Optimization opportunity** - Stop when 'a' becomes positive
4. **Edge cases matter** - Empty arrays, arrays with less than 3 elements
5. **Multiple solutions exist** - Be prepared to discuss trade-offs
6. **Time complexity** - Emphasize the improvement from O(n³) to O(n²)

### Common Follow-up Questions

1. **"How would you modify this for k-sum?"** - Generalize to finding k numbers that sum to target
2. **"What if we want the closest sum to zero?"** - Track minimum difference instead of exact match
3. **"Can you do this without sorting?"** - Discuss hash map approaches and their trade-offs
4. **"How do you handle integer overflow?"** - Consider using long for sum calculations

---
*This problem demonstrates the power of the two-pointer technique in reducing time complexity!*