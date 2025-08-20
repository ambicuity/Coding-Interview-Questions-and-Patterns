"""
Container With Most Water - Two Pointers Solution
Author: Ritesh Rana

Problem: Find two lines that can hold the most water.
Area = min(height[left], height[right]) × (right - left)

Time Complexity: O(n)
Space Complexity: O(1)
"""

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


def find_optimal_container(height: List[int]) -> tuple:
    """
    Find the indices and area of the optimal container.
    
    Returns:
        Tuple of (left_index, right_index, max_area)
    """
    left, right = 0, len(height) - 1
    max_water = 0
    best_left, best_right = 0, len(height) - 1
    
    while left < right:
        width = right - left
        current_height = min(height[left], height[right])
        current_area = width * current_height
        
        if current_area > max_water:
            max_water = current_area
            best_left, best_right = left, right
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return (best_left, best_right, max_water)


def test_max_area():
    """Test function with comprehensive test cases."""
    print("Testing Container With Most Water Solutions")
    print("=" * 55)
    
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
        },
        {
            'input': [2,3,10,5,7,8,9],
            'expected': 36,
            'description': 'Large peak'
        },
        {
            'input': [1,1000,1000,6,2,5,4,8,3,7],
            'expected': 1000,
            'description': 'Very large heights'
        }
    ]
    
    solutions = [
        ("Two Pointers", max_area),
        ("Brute Force", max_area_brute_force),
        ("Optimized Brute Force", max_area_optimized_brute_force)
    ]
    
    for i, test in enumerate(test_cases, 1):
        print(f"Test {i}: {test['description']}")
        print(f"Input: {test['input']}")
        print(f"Expected: {test['expected']}")
        
        all_correct = True
        for solution_name, solution_func in solutions:
            result = solution_func(test['input'])
            success = result == test['expected']
            status = "✓" if success else "✗"
            print(f"{solution_name}: {result} {status}")
            if not success:
                all_correct = False
        
        # Find optimal container details
        left_idx, right_idx, area = find_optimal_container(test['input'])
        print(f"Optimal container: indices {left_idx} and {right_idx}")
        print(f"  Heights: {test['input'][left_idx]} and {test['input'][right_idx]}")
        print(f"  Width: {right_idx - left_idx}")
        print(f"  Area: {area}")
        
        overall_status = "✓ ALL PASS" if all_correct else "✗ SOME FAIL"
        print(f"Overall: {overall_status}")
        print("-" * 55)
    
    # Performance comparison
    print("\nPerformance Test:")
    print("-" * 55)
    
    import time
    large_input = list(range(1, 1001)) + list(range(1000, 0, -1))  # 2000 elements
    
    print(f"Testing with {len(large_input)} elements")
    
    # Only test efficient algorithms for large input
    efficient_solutions = [
        ("Two Pointers", max_area),
        ("Optimized Brute Force", max_area_optimized_brute_force)
    ]
    
    for solution_name, solution_func in efficient_solutions:
        start_time = time.time()
        result = solution_func(large_input.copy())
        end_time = time.time()
        
        execution_time = (end_time - start_time) * 1000
        print(f"{solution_name}: {result} ({execution_time:.2f}ms)")


def demonstrate_algorithm():
    """Demonstrate the algorithm with a small example."""
    print("\n" + "=" * 55)
    print("Algorithm Demonstration")
    print("=" * 55)
    
    example = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(f"Example: {example}")
    print()
    
    result = max_area_with_visualization(example)
    print(f"Final Result: {result}")


def visual_representation(height: List[int]):
    """Create a visual representation of the container problem."""
    print("\n" + "=" * 55)
    print("Visual Representation")
    print("=" * 55)
    
    if not height:
        return
    
    max_height = max(height)
    print(f"Height array: {height}")
    print(f"Indices:      {list(range(len(height)))}")
    print()
    
    # Find optimal container
    left_idx, right_idx, area = find_optimal_container(height)
    print(f"Optimal container: indices {left_idx} and {right_idx} with area {area}")
    print()
    
    # Draw the container (simplified ASCII art)
    print("Container visualization:")
    for level in range(max_height, 0, -1):
        line = ""
        for i, h in enumerate(height):
            if h >= level:
                if i == left_idx or i == right_idx:
                    line += "|"  # Optimal container walls
                else:
                    line += "█"  # Other walls
            elif left_idx <= i <= right_idx and level <= min(height[left_idx], height[right_idx]):
                line += "~"  # Water
            else:
                line += " "  # Empty space
        print(f"{level:2d} {line}")
    
    print("   " + "".join(str(i % 10) for i in range(len(height))))
    print()
    print("Legend: | = optimal walls, █ = other walls, ~ = water")


if __name__ == "__main__":
    # Run comprehensive tests
    test_max_area()
    
    # Demonstrate algorithm
    demonstrate_algorithm()
    
    # Show visual representation
    visual_representation([1, 8, 6, 2, 5, 4, 8, 3, 7])
    
    # Interactive examples
    print("\n" + "=" * 55)
    print("Quick Examples:")
    
    examples = [
        [1, 8, 6, 2, 5, 4, 8, 3, 7],
        [1, 1],
        [1, 2, 1],
        [2, 1, 2]
    ]
    
    for example in examples:
        result = max_area(example)
        left_idx, right_idx, _ = find_optimal_container(example)
        print(f"{example} -> {result} (using indices {left_idx} and {right_idx})")