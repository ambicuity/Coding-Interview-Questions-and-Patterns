# Bit Manipulation Pattern

**Author:** Ritesh Rana

## Introduction to Bit Manipulation

Bit Manipulation involves algorithms that perform operations at the bit level of binary representations. These operations are fundamental to computer science and are extremely efficient since they work directly with the computer's binary system. Bit manipulation problems often require understanding binary properties, bitwise operators, and mathematical relationships in binary representation.

### Key Concepts

**Bitwise Operators:**
- **AND (&)**: Returns 1 if both bits are 1
- **OR (|)**: Returns 1 if at least one bit is 1  
- **XOR (^)**: Returns 1 if bits are different
- **NOT (~)**: Inverts all bits
- **Left Shift (<<)**: Shifts bits left, equivalent to multiplying by 2^n
- **Right Shift (>>)**: Shifts bits right, equivalent to dividing by 2^n

**Common Bit Tricks:**
- `x & 1`: Check if number is odd
- `x & (x-1)`: Remove rightmost set bit
- `x & -x`: Isolate rightmost set bit
- `x ^ x`: Always equals 0
- `x ^ 0`: Always equals x

### Common Patterns

1. **Bit Counting** - Count set bits (Hamming weight)
2. **Single Number** - Find unique element using XOR
3. **Bit Manipulation** - Set, clear, toggle specific bits
4. **Power of Two** - Check if number is power of 2
5. **Bit Reversal** - Reverse bit patterns
6. **Missing Numbers** - Find missing elements using XOR
7. **Subset Generation** - Generate all subsets using bit masks

### When to Use Bit Manipulation

- Space-efficient solutions needed
- Fast arithmetic operations required
- Checking number properties (even/odd, power of 2)
- Set operations on small universe
- Optimization problems with binary choices
- Low-level programming and embedded systems

### Advantages of Bit Manipulation

- **Speed**: Direct processor operations
- **Memory**: Compact representation
- **Elegance**: Often leads to clever solutions
- **Efficiency**: Constant time operations

## Problems Covered

1. Introduction to Bit Manipulation
2. Hamming Weights of Integers
3. Lonely Integer
4. Swap Odd and Even Bits

## Interview Tips for Bit Manipulation

💡 **Key Interview Tips:**

1. **Know the operators** - Understand all bitwise operators and their properties
2. **Think in binary** - Visualize numbers in binary representation
3. **Use bit tricks** - Learn common bit manipulation idioms
4. **Handle edge cases** - Zero, negative numbers, overflow conditions
5. **Practice with examples** - Work through problems step by step in binary

### Implementation Examples

**Count Set Bits (Hamming Weight):**
```python
def hamming_weight(n):
    count = 0
    while n:
        count += 1
        n &= n - 1  # Remove rightmost set bit
    return count

# Alternative using built-in
def hamming_weight_builtin(n):
    return bin(n).count('1')
```

**Single Number (Find Unique Element):**
```python
def single_number(nums):
    result = 0
    for num in nums:
        result ^= num  # XOR cancels out duplicates
    return result

# For finding single number when others appear twice
def single_number_three_times(nums):
    ones = twos = 0
    for num in nums:
        ones = (ones ^ num) & ~twos
        twos = (twos ^ num) & ~ones
    return ones
```

**Check if Power of Two:**
```python
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

# Alternative
def is_power_of_two_alt(n):
    return n > 0 and (n & -n) == n
```

**Reverse Bits:**
```python
def reverse_bits(n):
    result = 0
    for _ in range(32):  # Assuming 32-bit integer
        result = (result << 1) | (n & 1)
        n >>= 1
    return result
```

**Missing Number:**
```python
def missing_number(nums):
    n = len(nums)
    expected_xor = 0
    actual_xor = 0
    
    # XOR all numbers from 0 to n
    for i in range(n + 1):
        expected_xor ^= i
    
    # XOR all numbers in array
    for num in nums:
        actual_xor ^= num
    
    return expected_xor ^ actual_xor

# Alternative using sum
def missing_number_sum(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum
```

**Swap Odd and Even Bits:**
```python
def swap_odd_even_bits(n):
    # 0xAAAAAAAA = 10101010... (even positions)
    # 0x55555555 = 01010101... (odd positions)
    even_bits = n & 0xAAAAAAAA
    odd_bits = n & 0x55555555
    
    return (even_bits >> 1) | (odd_bits << 1)
```

**Generate All Subsets using Bit Mask:**
```python
def generate_subsets(nums):
    n = len(nums)
    subsets = []
    
    # Generate all numbers from 0 to 2^n - 1
    for mask in range(1 << n):  # 2^n combinations
        subset = []
        for i in range(n):
            if mask & (1 << i):  # Check if i-th bit is set
                subset.append(nums[i])
        subsets.append(subset)
    
    return subsets
```

**Add Two Numbers without Arithmetic Operators:**
```python
def add_without_plus(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a
```

### Bit Manipulation Tricks

**Set bit at position i:**
```python
def set_bit(n, i):
    return n | (1 << i)
```

**Clear bit at position i:**
```python
def clear_bit(n, i):
    return n & ~(1 << i)
```

**Toggle bit at position i:**
```python
def toggle_bit(n, i):
    return n ^ (1 << i)
```

**Check if bit at position i is set:**
```python
def is_bit_set(n, i):
    return (n & (1 << i)) != 0
```

### Advanced Techniques

**Brian Kernighan's Algorithm:**
Efficiently count set bits by removing rightmost set bit

**Bit Manipulation DP:**
Using bitmasks for dynamic programming on sets

**Gray Code:**
Binary numeral system where consecutive values differ by one bit

### Common Pitfalls and How to Avoid Them

1. **Integer Overflow**
   - Be aware of integer limits in different languages
   - Handle edge cases with maximum/minimum values

2. **Signed vs Unsigned**
   - Understand how negative numbers are represented
   - Be careful with right shifts on negative numbers

3. **Bit Position Confusion**
   - Remember bit positions are 0-indexed
   - Leftmost bit is most significant

4. **Operator Precedence**
   - Use parentheses to ensure correct order of operations
   - & and | have different precedence than == and !=

---
*Master bit manipulation to solve problems with elegant, efficient binary operations!*