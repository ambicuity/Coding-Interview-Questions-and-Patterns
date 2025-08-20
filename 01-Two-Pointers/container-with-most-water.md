# Container With Most Water

**Author:** Ritesh Rana

## Problem Statement

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i`th line are `(i, 0)` and `(i, height[i])`.

Find two lines that, together with the x-axis, form a container that can hold the most water.

Return the maximum amount of water a container can store.

**Note:** You may not slant the container.

### Examples

**Example 1:**
- **Input:** `height = [1,8,6,2,5,4,8,3,7]`
- **Output:** `49`
- **Explanation:** The lines at indices 1 and 8 form a container that can hold water of size 49.

**Example 2:**
- **Input:** `height = [1,1]`  
- **Output:** `1`
- **Explanation:** The two lines form a container with area 1.

**Example 3:**
- **Input:** `height = [1,2,1]`
- **Output:** `2`
- **Explanation:** Lines at indices 0 and 2 form a container with area 2.

## Intuition

The key insight is that the area formed by two lines is determined by:
- **Width:** Distance between the two lines (right - left)
- **Height:** Minimum of the two line heights (the water level)

**Area = min(height[left], height[right]) × (right - left)**

### Why Two Pointers Work

1. **Start with maximum width** - Place pointers at both ends
2. **Calculate current area** and track maximum
3. **Move the pointer with smaller height** - This is the key insight!
   - Moving the taller line inward can only decrease the area (smaller width, same height)
   - Moving the shorter line inward might increase the area (smaller width, but potentially taller height)

## Algorithm Steps

1. **Initialize pointers**: `left = 0`, `right = n-1`
2. **Calculate area**: `min(height[left], height[right]) × (right - left)`
3. **Update maximum area** if current is larger
4. **Move the pointer with smaller height** inward
5. **Repeat** until pointers meet

## Implementation

### Python Solution

```python
from typing import List

def max_area(height: List[int]) -> int:
    """
    Find maximum water container area using two pointers.
    
    Args:
        height: List of integers representing line heights
        
    Returns:
        Maximum area that can be formed
    """
    left, right = 0, len(height) - 1
    max_water = 0
    
    while left < right:
        # Calculate current area
        width = right - left
        current_height = min(height[left], height[right])
        current_area = width * current_height
        
        # Update maximum area
        max_water = max(max_water, current_area)
        
        # Move the pointer with smaller height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_water
```

### JavaScript Solution

```javascript
/**
 * Find maximum water container area using two pointers.
 * @param {number[]} height - Array of line heights
 * @returns {number} Maximum area that can be formed
 */
function maxArea(height) {
    let left = 0, right = height.length - 1;
    let maxWater = 0;
    
    while (left < right) {
        // Calculate current area
        const width = right - left;
        const currentHeight = Math.min(height[left], height[right]);
        const currentArea = width * currentHeight;
        
        // Update maximum area
        maxWater = Math.max(maxWater, currentArea);
        
        // Move the pointer with smaller height
        if (height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
    }
    
    return maxWater;
}
```

### Java Solution

```java
public int maxArea(int[] height) {
    int left = 0, right = height.length - 1;
    int maxWater = 0;
    
    while (left < right) {
        // Calculate current area
        int width = right - left;
        int currentHeight = Math.min(height[left], height[right]);
        int currentArea = width * currentHeight;
        
        // Update maximum area
        maxWater = Math.max(maxWater, currentArea);
        
        // Move the pointer with smaller height
        if (height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
    }
    
    return maxWater;
}
```

## Complexity Analysis

### Time Complexity
**O(n)** where n is the length of the array. We visit each element at most once.

### Space Complexity
**O(1)** - We only use constant extra space for pointers and variables.

## Why This Algorithm Works

### Mathematical Proof

Let's say we have the optimal solution with lines at positions `i` and `j` where `i < j`.

**Claim:** Our algorithm will consider this pair `(i, j)`.

**Proof by contradiction:**
1. Suppose our algorithm skips the optimal pair `(i, j)`
2. This happens if we move past `i` or `j` without considering them together
3. We only move a pointer when it has the smaller height
4. If we moved past `i`, it means `height[i] < height[k]` for some `k > i`
   - But then the pair `(i, j)` couldn't be optimal because `(k, j)` would have the same height but smaller width
5. Similar logic applies for `j`
6. Therefore, our algorithm must consider the optimal pair

### Visual Example

```
height = [1,8,6,2,5,4,8,3,7]
indices: [0,1,2,3,4,5,6,7,8]

Step 1: left=0, right=8
        Area = min(1,7) × 8 = 8
        Move left (1 < 7)

Step 2: left=1, right=8  
        Area = min(8,7) × 7 = 49  ← Maximum
        Move right (8 > 7)

Step 3: left=1, right=7
        Area = min(8,3) × 6 = 18
        Move right (8 > 3)

... continue until left >= right
```

## Alternative Approaches

### Brute Force Solution

```python
def max_area_brute_force(height: List[int]) -> int:
    """
    Brute force solution - O(n²) time complexity.
    """
    max_water = 0
    n = len(height)
    
    for i in range(n):
        for j in range(i + 1, n):
            width = j - i
            current_height = min(height[i], height[j])
            current_area = width * current_height
            max_water = max(max_water, current_area)
    
    return max_water
```

### Optimized Brute Force with Early Termination

```python
def max_area_optimized_brute_force(height: List[int]) -> int:
    """
    Optimized brute force with early termination.
    """
    max_water = 0
    n = len(height)
    
    for i in range(n):
        for j in range(n - 1, i, -1):  # Start from the end
            width = j - i
            current_height = min(height[i], height[j])
            current_area = width * current_height
            
            if current_area > max_water:
                max_water = current_area
            
            # Early termination: if current height equals height[i],
            # no need to check smaller widths with the same height
            if current_height == height[i]:
                break
    
    return max_water
```

## Edge Cases and Test Cases

### Comprehensive Test Suite

```python
def test_max_area():
    """Test function with various scenarios."""
    test_cases = [
        {
            'input': [1,8,6,2,5,4,8,3,7],
            'expected': 49,
            'description': 'Standard example'
        },
        {
            'input': [1,1],
            'expected': 1,
            'description': 'Two equal heights'
        },
        {
            'input': [1,2,1],
            'expected': 2,
            'description': 'Three elements'
        },
        {
            'input': [2,1,2],
            'expected': 4,
            'description': 'Peak in middle'
        },
        {
            'input': [1,2,3,4,5],
            'expected': 6,
            'description': 'Increasing heights'
        },
        {
            'input': [5,4,3,2,1],
            'expected': 6,
            'description': 'Decreasing heights'
        },
        {
            'input': [1,3,2,5,25,24,5],
            'expected': 24,
            'description': 'Mixed heights'
        },
        {
            'input': [0,1,0,2,1,0,1,3,2,1,2,1],
            'expected': 36,
            'description': 'Complex pattern'
        }
    ]
    
    for i, test in enumerate(test_cases, 1):
        result = max_area(test['input'])
        brute_result = max_area_brute_force(test['input'])
        
        success = result == test['expected'] == brute_result
        status = "✓ PASS" if success else "✗ FAIL"
        
        print(f"Test {i}: {test['description']}")
        print(f"Input: {test['input']}")
        print(f"Expected: {test['expected']}")
        print(f"Two Pointers: {result}")
        print(f"Brute Force: {brute_result}")
        print(f"Result: {status}")
        print("-" * 50)
```

### Edge Cases to Consider

| Input | Expected | Description |
|-------|----------|-------------|
| `[1,1]` | `1` | Minimum input size |
| `[0,2]` | `0` | One height is zero |
| `[1000,1000]` | `1000` | Very large equal heights |
| `[1,2,3,4,5]` | `6` | Strictly increasing |
| `[5,4,3,2,1]` | `6` | Strictly decreasing |

## Interview Tips for Container With Most Water

💡 **Key Points to Remember:**

1. **Understand the problem** - Area calculation with min height as limiting factor
2. **Start with brute force** - Then optimize with two pointers
3. **Explain the key insight** - Why moving the shorter line makes sense
4. **Handle edge cases** - Array with 2 elements, equal heights, zero heights
5. **Trace through example** - Show how the algorithm finds the optimal solution

### Common Follow-up Questions

1. **"What if we can use multiple containers?"** - This becomes a different problem
2. **"What if lines can be slanted?"** - Changes the area calculation completely
3. **"How would you handle 3D containers?"** - Extends to volume calculation
4. **"What if there's a cost to using each line?"** - Becomes an optimization problem

### Algorithm Visualization

```python
def max_area_with_visualization(height: List[int]) -> int:
    """
    Container with most water with step-by-step visualization.
    """
    left, right = 0, len(height) - 1
    max_water = 0
    step = 1
    
    print(f"Height array: {height}")
    print(f"Indices:      {list(range(len(height)))}")
    print()
    
    while left < right:
        width = right - left
        current_height = min(height[left], height[right])
        current_area = width * current_height
        
        print(f"Step {step}:")
        print(f"  Left: index {left}, height {height[left]}")
        print(f"  Right: index {right}, height {height[right]}")
        print(f"  Width: {width}")
        print(f"  Height: min({height[left]}, {height[right]}) = {current_height}")
        print(f"  Area: {width} × {current_height} = {current_area}")
        
        if current_area > max_water:
            max_water = current_area
            print(f"  New maximum: {max_water}")
        else:
            print(f"  Current max: {max_water}")
        
        # Move pointer
        if height[left] < height[right]:
            print(f"  Moving left pointer (smaller height)")
            left += 1
        else:
            print(f"  Moving right pointer (smaller/equal height)")
            right -= 1
        
        print()
        step += 1
    
    return max_water
```

## Related Problems

- **Trapping Rain Water** - Different problem but similar two-pointer technique
- **Largest Rectangle in Histogram** - Uses stack instead of two pointers
- **Maximum Rectangle** - 2D version of the problem
- **Water and Jug Problem** - Different type of container problem

## Common Mistakes to Avoid

❌ **Don't move both pointers** - Only move the one with smaller height
❌ **Don't forget the area formula** - It's width × min(height)
❌ **Don't use nested loops** - Two pointers give O(n) solution
❌ **Don't overthink the proof** - Trust that moving shorter pointer is optimal
❌ **Don't ignore edge cases** - Handle arrays of size 2, zero heights

---
*This problem beautifully demonstrates how mathematical insight can lead to an elegant O(n) solution!*