# Valid Palindrome

**Author:** Ritesh Rana

## Problem Statement

A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

### Examples

**Example 1:**
- **Input:** `s = "A man, a plan, a canal: Panama"`
- **Output:** `true`
- **Explanation:** "amanaplanacanalpanama" is a palindrome.

**Example 2:**
- **Input:** `s = "race a car"`
- **Output:** `false`  
- **Explanation:** "raceacar" is not a palindrome.

**Example 3:**
- **Input:** `s = " "`
- **Output:** `true`
- **Explanation:** After removing non-alphanumeric characters, s becomes an empty string "", which reads the same forward and backward.

## Intuition

The key insight is to use two pointers - one starting from the beginning and one from the end of the string. We compare characters while:

1. **Skipping non-alphanumeric characters**
2. **Converting to lowercase for case-insensitive comparison**
3. **Moving pointers toward each other**

If we find any mismatch, it's not a palindrome. If pointers cross without finding a mismatch, it's a palindrome.

## Algorithm Steps

1. **Initialize two pointers**: `left` at start (0), `right` at end (n-1)
2. **Skip non-alphanumeric characters** on both sides
3. **Compare characters** (case-insensitive)
4. **Move pointers** inward if characters match
5. **Return false** if mismatch found, **true** if all characters match

## Implementation

### Python Solution

```python
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
```

### JavaScript Solution

```javascript
/**
 * Check if string is a valid palindrome using two pointers.
 * @param {string} s - Input string to check
 * @returns {boolean} True if palindrome, false otherwise
 */
function isPalindrome(s) {
    let left = 0, right = s.length - 1;
    
    while (left < right) {
        // Skip non-alphanumeric characters from left
        while (left < right && !isAlphanumeric(s[left])) {
            left++;
        }
        
        // Skip non-alphanumeric characters from right
        while (left < right && !isAlphanumeric(s[right])) {
            right--;
        }
        
        // Compare characters (case-insensitive)
        if (s[left].toLowerCase() !== s[right].toLowerCase()) {
            return false;
        }
        
        left++;
        right--;
    }
    
    return true;
}

/**
 * Helper function to check if character is alphanumeric.
 * @param {string} char - Character to check
 * @returns {boolean} True if alphanumeric
 */
function isAlphanumeric(char) {
    return /^[a-zA-Z0-9]$/.test(char);
}
```

### Java Solution

```java
public boolean isPalindrome(String s) {
    int left = 0, right = s.length() - 1;
    
    while (left < right) {
        // Skip non-alphanumeric characters from left
        while (left < right && !Character.isLetterOrDigit(s.charAt(left))) {
            left++;
        }
        
        // Skip non-alphanumeric characters from right
        while (left < right && !Character.isLetterOrDigit(s.charAt(right))) {
            right--;
        }
        
        // Compare characters (case-insensitive)
        if (Character.toLowerCase(s.charAt(left)) != 
            Character.toLowerCase(s.charAt(right))) {
            return false;
        }
        
        left++;
        right--;
    }
    
    return true;
}
```

## Complexity Analysis

### Time Complexity
**O(n)** where n is the length of the string. We traverse the string at most once with both pointers.

### Space Complexity
**O(1)** - We only use constant extra space for the two pointers and variables.

## Alternative Approaches

### Approach 1: Clean and Reverse (Less Efficient)

```python
def is_palindrome_clean_reverse(s: str) -> bool:
    """
    Clean string first, then compare with reverse.
    Time: O(n), Space: O(n)
    """
    # Clean string: keep only alphanumeric, convert to lowercase
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    
    # Compare with reverse
    return cleaned == cleaned[::-1]
```

### Approach 2: Recursive Two Pointers

```python
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
```

## Edge Cases and Test Cases

### Comprehensive Test Suite

```python
def test_is_palindrome():
    """Test function with various scenarios."""
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
        }
    ]
    
    for i, test in enumerate(test_cases, 1):
        result = is_palindrome(test['input'])
        success = result == test['expected']
        status = "✓ PASS" if success else "✗ FAIL"
        
        print(f"Test {i}: {test['description']}")
        print(f"Input: \"{test['input']}\"")
        print(f"Expected: {test['expected']}")
        print(f"Got: {result}")
        print(f"Result: {status}")
        print("-" * 50)
```

### Edge Cases to Consider

| Input | Expected | Description |
|-------|----------|-------------|
| `""` | `True` | Empty string |
| `" "` | `True` | Only whitespace |
| `"a"` | `True` | Single character |
| `"ab"` | `False` | Two different characters |
| `"12321"` | `True` | Numeric palindrome |
| `"A1B2b1a"` | `True` | Mixed alphanumeric |

## Interview Tips for Valid Palindrome

💡 **Key Points to Remember:**

1. **Clarify requirements** - Case sensitivity, what characters to consider
2. **Handle edge cases** - Empty strings, single characters, only punctuation
3. **Two-pointer technique** - More space-efficient than creating cleaned string
4. **Character checking** - Use built-in functions for alphanumeric checks
5. **Case conversion** - Convert to same case for comparison

### Common Follow-up Questions

1. **"What if we can remove at most one character?"** - Valid Palindrome II
2. **"What about palindromic substrings?"** - Count or find all palindromic substrings
3. **"How would you handle Unicode characters?"** - Discuss normalization and locale
4. **"What if memory is extremely limited?"** - Emphasize O(1) space advantage

### Optimization Notes

```python
# More efficient character checking
def is_alphanumeric_fast(char: str) -> bool:
    """Fast alphanumeric check without regex."""
    return ('a' <= char <= 'z' or 
            'A' <= char <= 'Z' or 
            '0' <= char <= '9')

# Alternative using ASCII values
def to_lowercase_fast(char: str) -> str:
    """Fast lowercase conversion."""
    if 'A' <= char <= 'Z':
        return chr(ord(char) + 32)
    return char
```

## Related Problems

- **Valid Palindrome II** - Remove at most one character
- **Palindromic Substrings** - Count all palindromic substrings
- **Longest Palindromic Substring** - Find the longest palindrome
- **Palindrome Partitioning** - Partition string into palindromes

## Common Mistakes to Avoid

❌ **Don't create a cleaned string first** - Uses extra O(n) space
❌ **Don't forget edge cases** - Empty strings, single characters
❌ **Don't ignore case sensitivity** - Convert to same case
❌ **Don't use regex unnecessarily** - Simple character checks are faster
❌ **Don't forget to increment both pointers** - Leads to infinite loops

---
*The two-pointer technique shines in palindrome problems - master this pattern for string manipulation interviews!*