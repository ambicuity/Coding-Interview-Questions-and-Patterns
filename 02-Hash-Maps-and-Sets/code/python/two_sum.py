"""
Two Sum (Pair Sum - Unsorted) - Hash Map Solution
Author: Ritesh Rana

Problem: Given an array of integers and a target, return indices of two numbers 
that add up to the target.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List, Dict
from collections import Counter


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


def two_sum_all_pairs(nums: List[int], target: int) -> List[List[int]]:
    """
    Find all pairs that sum to target (for cases with multiple solutions).
    """
    seen = {}
    pairs = []
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in seen:
            # Found a pair - add all combinations with previous occurrences
            for prev_index in seen[complement]:
                pairs.append([prev_index, i])
        
        # Store this number and its index
        if num not in seen:
            seen[num] = []
        seen[num].append(i)
    
    return pairs


def two_sum_counter(nums: List[int], target: int) -> List[int]:
    """
    Alternative using Counter for educational purposes.
    """
    counter = Counter(nums)
    num_to_first_index = {}
    num_to_second_index = {}
    
    # Build index mappings
    for i, num in enumerate(nums):
        if num not in num_to_first_index:
            num_to_first_index[num] = i
        else:
            num_to_second_index[num] = i
    
    for num in counter:
        complement = target - num
        
        if complement in counter:
            if complement == num and counter[num] >= 2:
                # Same number used twice
                return [num_to_first_index[num], num_to_second_index[num]]
            elif complement != num:
                return sorted([num_to_first_index[num], num_to_first_index[complement]])
    
    return []


def two_sum_with_trace(nums: List[int], target: int) -> List[int]:
    """
    Two sum with step-by-step trace for educational purposes.
    """
    seen = {}
    print(f"Finding two numbers in {nums} that sum to {target}")
    print("Step-by-step trace:")
    print()
    
    for i, num in enumerate(nums):
        complement = target - num
        
        print(f"Step {i + 1}: index={i}, num={num}")
        print(f"  Looking for complement: {target} - {num} = {complement}")
        print(f"  Current seen: {seen}")
        
        if complement in seen:
            result = [seen[complement], i]
            print(f"  ✓ Found complement {complement} at index {seen[complement]}")
            print(f"  Solution: indices {result}")
            return result
        
        seen[num] = i
        print(f"  Added {num} at index {i} to seen")
        print()
    
    print("No solution found")
    return []


def test_two_sum():
    """Test function with comprehensive test cases."""
    print("Testing Two Sum (Pair Sum - Unsorted) Solutions")
    print("=" * 60)
    
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
        },
        {
            'nums': [1, 5, 5, 11],
            'target': 10,
            'expected': [1, 2],
            'description': 'Duplicate elements in middle'
        },
        {
            'nums': [230, 863, 916, 585, 981, 404, 316, 785, 88, 12, 70, 435, 384, 778, 887, 755],
            'target': 542,
            'expected': [0, 12],  # 230 + 70 = 300... wait, let me check this
            'description': 'Large array test'
        }
    ]
    
    solutions = [
        ("Hash Map", two_sum),
        ("Brute Force", two_sum_brute_force),
        ("Sort + Two Pointers", two_sum_sorted),
        ("Counter Method", two_sum_counter)
    ]
    
    # Fix the large array test case
    test_cases[9]['nums'] = [230, 863, 916, 585, 981, 404, 316, 785, 88, 12, 312, 435, 384, 778, 887, 755]
    test_cases[9]['expected'] = [0, 10]  # 230 + 312 = 542
    
    for i, test in enumerate(test_cases, 1):
        print(f"Test {i}: {test['description']}")
        print(f"Input: nums = {test['nums']}, target = {test['target']}")
        
        all_correct = True
        results = {}
        
        for solution_name, solution_func in solutions:
            try:
                result = solution_func(test['nums'].copy(), test['target'])
                
                # Verify that the result is correct
                if result and len(result) == 2:
                    actual_sum = test['nums'][result[0]] + test['nums'][result[1]]
                    success = (actual_sum == test['target'] and 
                              result[0] != result[1] and 
                              0 <= result[0] < len(test['nums']) and 
                              0 <= result[1] < len(test['nums']))
                else:
                    success = False
                
                status = "✓" if success else "✗"
                results[solution_name] = (result, success)
                print(f"{solution_name}: {result} {status}")
                
                if not success:
                    all_correct = False
                    
            except Exception as e:
                print(f"{solution_name}: ERROR - {e}")
                all_correct = False
        
        # Verify one of the results
        if results.get("Hash Map", (None, False))[1]:
            result = results["Hash Map"][0]
            verification_sum = test['nums'][result[0]] + test['nums'][result[1]]
            print(f"Verification: nums[{result[0]}] + nums[{result[1]}] = {test['nums'][result[0]]} + {test['nums'][result[1]]} = {verification_sum}")
        
        overall_status = "✓ ALL PASS" if all_correct else "✗ SOME FAIL"
        print(f"Overall: {overall_status}")
        print("-" * 60)
    
    # Test all pairs function
    print("\nTesting All Pairs Function:")
    print("-" * 60)
    
    multi_solution_case = [1, 2, 3, 4, 5, 6]
    target = 7
    all_pairs = two_sum_all_pairs(multi_solution_case, target)
    
    print(f"Array: {multi_solution_case}, Target: {target}")
    print(f"All pairs that sum to {target}:")
    for pair in all_pairs:
        val1, val2 = multi_solution_case[pair[0]], multi_solution_case[pair[1]]
        print(f"  Indices {pair}: {val1} + {val2} = {val1 + val2}")


def demonstrate_algorithm():
    """Demonstrate the algorithm step by step."""
    print("\n" + "=" * 60)
    print("Algorithm Demonstration")
    print("=" * 60)
    
    example = [2, 7, 11, 15]
    target = 9
    
    print("Two Sum Algorithm - Step by Step:")
    result = two_sum_with_trace(example, target)
    
    print(f"\nFinal result: {result}")


def performance_comparison():
    """Compare performance of different approaches."""
    print("\n" + "=" * 60)
    print("Performance Comparison")
    print("=" * 60)
    
    import time
    import random
    
    # Generate large test case
    large_nums = random.sample(range(-10000, 10000), 2000)
    target = large_nums[100] + large_nums[500]  # Ensure solution exists
    
    approaches = [
        ("Hash Map", two_sum),
        ("Sort + Two Pointers", two_sum_sorted)
        # Skip brute force for large input as it would be too slow
    ]
    
    print(f"Testing with {len(large_nums)} elements")
    print(f"Target: {target}")
    
    for approach_name, approach_func in approaches:
        start_time = time.time()
        result = approach_func(large_nums.copy(), target)
        end_time = time.time()
        
        execution_time = (end_time - start_time) * 1000  # milliseconds
        
        # Verify result
        if result:
            actual_sum = large_nums[result[0]] + large_nums[result[1]]
            success = actual_sum == target
        else:
            success = False
        
        status = "✓" if success else "✗"
        print(f"{approach_name}: {success} {status} ({execution_time:.2f}ms)")


if __name__ == "__main__":
    # Run comprehensive tests
    test_two_sum()
    
    # Demonstrate algorithm
    demonstrate_algorithm()
    
    # Performance comparison
    performance_comparison()
    
    # Interactive examples
    print("\n" + "=" * 60)
    print("Quick Examples:")
    
    examples = [
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6),
        ([3, 3], 6),
        ([-1, 2, 1, -4], 0)
    ]
    
    for nums, target in examples:
        result = two_sum(nums, target)
        if result:
            print(f"{nums}, target={target} -> indices {result} (values: {nums[result[0]]}, {nums[result[1]]})")
        else:
            print(f"{nums}, target={target} -> No solution")