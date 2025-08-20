"""
Triplet Sum - Two Pointers Solution
Author: Ritesh Rana

Problem: Given an array of integers, return all triplets [a, b, c] such that a + b + c = 0.
The solution must not contain duplicate triplets.

Time Complexity: O(n²)
Space Complexity: O(n) - not counting output space
"""

from typing import List


def triplet_sum(nums: List[int]) -> List[List[int]]:
    """
    Find all triplets that sum to zero using two-pointer technique.
    
    Args:
        nums: List of integers
        
    Returns:
        List of triplets [a, b, c] where a + b + c = 0
    """
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
    """
    Find all pairs in sorted array that sum to target value.
    
    Args:
        nums: Sorted list of integers
        start: Starting index for the search
        target: Target sum value
        
    Returns:
        List of pairs [b, c] where b + c = target
    """
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


def triplet_sum_brute_force(nums: List[int]) -> List[List[int]]:
    """
    Brute force solution for comparison - O(n³) time complexity.
    """
    n = len(nums)
    triplets = set()
    
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                    triplets.add(triplet)
    
    return [list(triplet) for triplet in triplets]


def test_triplet_sum():
    """Test function with comprehensive test cases."""
    print("Testing Triplet Sum Solutions")
    print("=" * 40)
    
    test_cases = [
        {
            'input': [0, -1, 2, -3, 1],
            'expected': [[-3, 1, 2], [-1, 0, 1]],
            'description': 'Basic example'
        },
        {
            'input': [],
            'expected': [],
            'description': 'Empty array'
        },
        {
            'input': [0],
            'expected': [],
            'description': 'Single element'
        },
        {
            'input': [1, -1],
            'expected': [],
            'description': 'Two elements'
        },
        {
            'input': [0, 0, 0],
            'expected': [[0, 0, 0]],
            'description': 'All same values'
        },
        {
            'input': [1, 0, 1],
            'expected': [],
            'description': 'No valid triplets'
        },
        {
            'input': [0, 0, 1, -1, 1, -1],
            'expected': [[-1, 0, 1]],
            'description': 'Duplicate triplets'
        },
        {
            'input': [-1, 0, 1, 2, -1, -4],
            'expected': [[-1, -1, 2], [-1, 0, 1]],
            'description': 'Complex case'
        }
    ]
    
    for i, test in enumerate(test_cases, 1):
        # Test optimized solution
        result = triplet_sum(test['input'].copy())
        result_sorted = sorted([sorted(triplet) for triplet in result])
        expected_sorted = sorted([sorted(triplet) for triplet in test['expected']])
        
        success = result_sorted == expected_sorted
        status = "✓ PASS" if success else "✗ FAIL"
        
        print(f"Test {i}: {test['description']}")
        print(f"Input: {test['input']}")
        print(f"Expected: {test['expected']}")
        print(f"Got: {result}")
        print(f"Result: {status}")
        
        # Test brute force for comparison (only for small inputs)
        if len(test['input']) <= 6:
            brute_result = triplet_sum_brute_force(test['input'].copy())
            brute_sorted = sorted([sorted(triplet) for triplet in brute_result])
            brute_match = brute_sorted == expected_sorted
            print(f"Brute force match: {'✓' if brute_match else '✗'}")
        
        print("-" * 40)


if __name__ == "__main__":
    # Run comprehensive tests
    test_triplet_sum()
    
    # Interactive example
    print("\nInteractive Example:")
    example_input = [0, -1, 2, -3, 1]
    print(f"Input: {example_input}")
    result = triplet_sum(example_input)
    print(f"Triplets that sum to zero: {result}")