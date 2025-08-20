"""
Pair Sum - Sorted: Two Pointers Solution
Author: Ritesh Rana

Problem: Given a sorted array and target sum, find two numbers that add up to target.
Return 1-indexed positions of the two numbers.

Time Complexity: O(n)
Space Complexity: O(1)
"""

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


def pair_sum_sorted_all_pairs(nums: List[int], target: int) -> List[List[int]]:
    """
    Find all pairs in sorted array that sum to target.
    
    Args:
        nums: Sorted list of integers
        target: Target sum value
        
    Returns:
        List of 1-indexed position pairs
    """
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


def pair_sum_sorted_values(nums: List[int], target: int) -> Optional[List[int]]:
    """
    Return the actual values instead of indices.
    
    Args:
        nums: Sorted list of integers
        target: Target sum value
        
    Returns:
        List of values that sum to target, or None if not found
    """
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


def pair_sum_unsorted(nums: List[int], target: int) -> Optional[List[int]]:
    """
    Find pair sum in unsorted array using hash map.
    
    Args:
        nums: List of integers (unsorted)
        target: Target sum value
        
    Returns:
        1-indexed positions of the two numbers, or None if not found
    """
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement] + 1, i + 1]  # 1-indexed
        seen[num] = i
    
    return None


def test_pair_sum_sorted():
    """Test function with comprehensive test cases."""
    print("Testing Pair Sum - Sorted Solutions")
    print("=" * 45)
    
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
            'description': 'Multiple valid pairs'
        },
        {
            'nums': [1, 2],
            'target': 5,
            'expected': None,
            'description': 'No solution exists'
        },
        {
            'nums': [1, 1, 1, 1],
            'target': 2,
            'expected': [1, 4],
            'description': 'All same elements'
        },
        {
            'nums': [-3, -1, 0, 2],
            'target': -1,
            'expected': [1, 4],
            'description': 'Mixed positive/negative'
        }
    ]
    
    for i, test in enumerate(test_cases, 1):
        result = pair_sum_sorted(test['nums'].copy(), test['target'])
        success = result == test['expected']
        status = "✓ PASS" if success else "✗ FAIL"
        
        print(f"Test {i}: {test['description']}")
        print(f"Input: nums = {test['nums']}, target = {test['target']}")
        print(f"Expected: {test['expected']}")
        print(f"Got: {result}")
        print(f"Result: {status}")
        
        # Test values version
        values_result = pair_sum_sorted_values(test['nums'].copy(), test['target'])
        if test['expected'] is not None:
            expected_values = [test['nums'][test['expected'][0]-1], test['nums'][test['expected'][1]-1]]
            values_match = values_result == expected_values
        else:
            values_match = values_result is None
        print(f"Values version: {values_result} {'✓' if values_match else '✗'}")
        
        print("-" * 45)
    
    # Test all pairs function
    print("\nTesting All Pairs Function:")
    print("-" * 45)
    
    # Array with multiple valid pairs
    nums_multi = [1, 2, 3, 4, 5, 6]
    target_multi = 7
    all_pairs = pair_sum_sorted_all_pairs(nums_multi, target_multi)
    print(f"Array: {nums_multi}, Target: {target_multi}")
    print(f"All pairs: {all_pairs}")
    
    # Verify each pair
    for pair in all_pairs:
        val1, val2 = nums_multi[pair[0]-1], nums_multi[pair[1]-1]
        print(f"Pair {pair}: {val1} + {val2} = {val1 + val2}")
    
    print("-" * 45)
    
    # Test hash map approach for unsorted
    print("\nTesting Hash Map Approach (Unsorted):")
    print("-" * 45)
    
    unsorted_test = {
        'nums': [11, 2, 15, 7],  # Unsorted version of first test
        'target': 9,
        'expected': [2, 4],  # Different indices due to unsorted array
        'description': 'Unsorted array'
    }
    
    unsorted_result = pair_sum_unsorted(unsorted_test['nums'], unsorted_test['target'])
    print(f"Unsorted: {unsorted_test['nums']}, Target: {unsorted_test['target']}")
    print(f"Result: {unsorted_result}")
    
    # Verify the result
    if unsorted_result:
        val1 = unsorted_test['nums'][unsorted_result[0]-1]
        val2 = unsorted_test['nums'][unsorted_result[1]-1]
        print(f"Verification: {val1} + {val2} = {val1 + val2}")


if __name__ == "__main__":
    # Run comprehensive tests
    test_pair_sum_sorted()
    
    # Interactive example
    print("\n" + "=" * 45)
    print("Interactive Example:")
    example_nums = [2, 7, 11, 15]
    example_target = 9
    print(f"Find two numbers in {example_nums} that sum to {example_target}")
    
    result = pair_sum_sorted(example_nums, example_target)
    if result:
        print(f"Found at positions: {result}")
        print(f"Values: {example_nums[result[0]-1]} + {example_nums[result[1]-1]} = {example_target}")
    else:
        print("No solution found")