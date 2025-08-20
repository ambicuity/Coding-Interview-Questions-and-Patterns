"""
Valid Palindrome - Two Pointers Solution
Author: Ritesh Rana

Problem: Check if a string is a valid palindrome after converting to lowercase 
and removing all non-alphanumeric characters.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def is_palindrome(s: str) -> bool:
    """
    Check if string is a valid palindrome using two pointers.
    
    Args:
        s: Input string to check
        
    Returns:
        True if string is a palindrome, False otherwise
    """
    left, right = 0, len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric characters from left
        while left < right and not s[left].isalnum():
            left += 1
        
        # Skip non-alphanumeric characters from right
        while left < right and not s[right].isalnum():
            right -= 1
        
        # Compare characters (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True


def is_palindrome_clean_reverse(s: str) -> bool:
    """
    Clean string first, then compare with reverse.
    Time: O(n), Space: O(n) - Less efficient but more readable.
    """
    # Clean string: keep only alphanumeric, convert to lowercase
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    
    # Compare with reverse
    return cleaned == cleaned[::-1]


def is_palindrome_recursive(s: str) -> bool:
    """
    Recursive implementation of two pointers approach.
    """
    def helper(left: int, right: int) -> bool:
        if left >= right:
            return True
        
        # Skip non-alphanumeric from left
        while left < right and not s[left].isalnum():
            left += 1
        
        # Skip non-alphanumeric from right
        while left < right and not s[right].isalnum():
            right -= 1
        
        # Check current characters
        if s[left].lower() != s[right].lower():
            return False
        
        return helper(left + 1, right - 1)
    
    return helper(0, len(s) - 1)


def is_alphanumeric_fast(char: str) -> bool:
    """Fast alphanumeric check without using built-in methods."""
    return ('a' <= char <= 'z' or 
            'A' <= char <= 'Z' or 
            '0' <= char <= '9')


def to_lowercase_fast(char: str) -> str:
    """Fast lowercase conversion using ASCII values."""
    if 'A' <= char <= 'Z':
        return chr(ord(char) + 32)
    return char


def is_palindrome_optimized(s: str) -> bool:
    """
    Optimized version using custom character checking functions.
    """
    left, right = 0, len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric characters from left
        while left < right and not is_alphanumeric_fast(s[left]):
            left += 1
        
        # Skip non-alphanumeric characters from right
        while left < right and not is_alphanumeric_fast(s[right]):
            right -= 1
        
        # Compare characters (case-insensitive)
        if to_lowercase_fast(s[left]) != to_lowercase_fast(s[right]):
            return False
        
        left += 1
        right -= 1
    
    return True


def test_is_palindrome():
    """Test function with comprehensive test cases."""
    print("Testing Valid Palindrome Solutions")
    print("=" * 50)
    
    test_cases = [
        {
            'input': "A man, a plan, a canal: Panama",
            'expected': True,
            'description': 'Classic palindrome with punctuation'
        },
        {
            'input': "race a car",
            'expected': False,
            'description': 'Not a palindrome'
        },
        {
            'input': " ",
            'expected': True,
            'description': 'Only spaces'
        },
        {
            'input': "",
            'expected': True,
            'description': 'Empty string'
        },
        {
            'input': "a",
            'expected': True,
            'description': 'Single character'
        },
        {
            'input': "Madam",
            'expected': True,
            'description': 'Case insensitive'
        },
        {
            'input': "No 'x' in Nixon",
            'expected': True,
            'description': 'Complex punctuation'
        },
        {
            'input': "Mr. Owl ate my metal worm",
            'expected': True,
            'description': 'Long palindrome'
        },
        {
            'input': "1221",
            'expected': True,
            'description': 'Numeric palindrome'
        },
        {
            'input': "A Santa at NASA",
            'expected': True,
            'description': 'Mixed alphanumeric'
        },
        {
            'input': "Was it a car or a cat I saw?",
            'expected': True,
            'description': 'Palindrome with question mark'
        },
        {
            'input': "12ab21",
            'expected': False,
            'description': 'Mixed alphanumeric - not palindrome'
        }
    ]
    
    solutions = [
        ("Two Pointers", is_palindrome),
        ("Clean & Reverse", is_palindrome_clean_reverse),
        ("Recursive", is_palindrome_recursive),
        ("Optimized", is_palindrome_optimized)
    ]
    
    for i, test in enumerate(test_cases, 1):
        print(f"Test {i}: {test['description']}")
        print(f"Input: \"{test['input']}\"")
        print(f"Expected: {test['expected']}")
        
        all_correct = True
        for solution_name, solution_func in solutions:
            result = solution_func(test['input'])
            success = result == test['expected']
            status = "✓" if success else "✗"
            print(f"{solution_name}: {result} {status}")
            if not success:
                all_correct = False
        
        overall_status = "✓ ALL PASS" if all_correct else "✗ SOME FAIL"
        print(f"Overall: {overall_status}")
        print("-" * 50)
    
    # Performance comparison for longer strings
    print("\nPerformance Test with Long String:")
    print("-" * 50)
    long_palindrome = "A man a plan a canal Panama" * 100
    long_not_palindrome = "This is not a palindrome" * 100
    
    test_strings = [
        ("Long palindrome", long_palindrome, True),
        ("Long non-palindrome", long_not_palindrome, False)
    ]
    
    import time
    
    # Skip recursive for performance tests (hits recursion limit)
    perf_solutions = [
        ("Two Pointers", is_palindrome),
        ("Clean & Reverse", is_palindrome_clean_reverse),
        ("Optimized", is_palindrome_optimized)
    ]
    
    for name, test_str, expected in test_strings:
        print(f"\nTesting: {name} (length: {len(test_str)})")
        
        for solution_name, solution_func in perf_solutions:
            start_time = time.time()
            result = solution_func(test_str)
            end_time = time.time()
            
            execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
            status = "✓" if result == expected else "✗"
            print(f"{solution_name}: {result} {status} ({execution_time:.2f}ms)")


def demonstrate_algorithm():
    """Demonstrate the algorithm step by step."""
    print("\n" + "=" * 50)
    print("Algorithm Demonstration")
    print("=" * 50)
    
    test_string = "A man, a plan, a canal: Panama"
    print(f"Input: \"{test_string}\"")
    print("\nStep-by-step execution:")
    
    left, right = 0, len(test_string) - 1
    step = 1
    
    while left < right:
        # Show current positions
        print(f"\nStep {step}:")
        print(f"Left pointer at index {left}: '{test_string[left]}'")
        print(f"Right pointer at index {right}: '{test_string[right]}'")
        
        # Skip non-alphanumeric from left
        original_left = left
        while left < right and not test_string[left].isalnum():
            left += 1
        if left != original_left:
            print(f"Skipped non-alphanumeric, left now at {left}: '{test_string[left]}'")
        
        # Skip non-alphanumeric from right
        original_right = right
        while left < right and not test_string[right].isalnum():
            right -= 1
        if right != original_right:
            print(f"Skipped non-alphanumeric, right now at {right}: '{test_string[right]}'")
        
        if left < right:
            left_char = test_string[left].lower()
            right_char = test_string[right].lower()
            print(f"Comparing: '{left_char}' vs '{right_char}'")
            
            if left_char != right_char:
                print("Mismatch found! Not a palindrome.")
                return
            else:
                print("Match! Continue...")
            
            left += 1
            right -= 1
        
        step += 1
        
        if step > 10:  # Prevent too much output
            print("... (continuing)")
            break
    
    print(f"\nResult: The string IS a palindrome!")


if __name__ == "__main__":
    # Run comprehensive tests
    test_is_palindrome()
    
    # Demonstrate algorithm
    demonstrate_algorithm()
    
    # Interactive example
    print("\n" + "=" * 50)
    print("Interactive Examples:")
    
    examples = [
        "A man, a plan, a canal: Panama",
        "race a car",
        "Madam",
        ""
    ]
    
    for example in examples:
        result = is_palindrome(example)
        print(f"'{example}' -> {result}")
        
        # Show cleaned version
        cleaned = ''.join(char.lower() for char in example if char.isalnum())
        print(f"  Cleaned: '{cleaned}'")
        print(f"  Reversed: '{cleaned[::-1]}'")
        print(f"  Same? {cleaned == cleaned[::-1]}")
        print()