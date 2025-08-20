# Dynamic Programming Pattern

**Author:** Ritesh Rana

## Introduction to Dynamic Programming

Dynamic Programming (DP) is an algorithmic technique for solving optimization problems by breaking them down into simpler subproblems and storing the results to avoid redundant calculations. It combines the correctness of exhaustive search with the efficiency of memoization, making it essential for solving complex optimization problems.

### Key Concepts

**Core Principles:**
- **Optimal Substructure**: Optimal solution contains optimal solutions to subproblems
- **Overlapping Subproblems**: Same subproblems solved multiple times
- **Memoization**: Store solutions to avoid recomputation
- **Bottom-up vs Top-down**: Build solutions from base cases vs recursive with memoization

**DP Approaches:**
1. **Memoization (Top-down)**: Recursive with caching
2. **Tabulation (Bottom-up)**: Iterative table filling
3. **Space Optimization**: Reduce space complexity when possible

### Common Patterns

1. **Linear DP** - 1D array problems (Fibonacci, climbing stairs)
2. **Grid DP** - 2D matrix problems (paths, edit distance)
3. **Sequence DP** - String/array subsequence problems
4. **Knapsack DP** - Resource optimization problems
5. **Interval DP** - Range-based optimization
6. **Tree DP** - Optimization on tree structures
7. **Digit DP** - Problems involving number digits

### When to Use Dynamic Programming

- Optimization problems (max/min)
- Counting problems (number of ways)
- Decision problems (yes/no with optimal choices)
- Problems with overlapping subproblems
- When brute force has exponential time complexity

### DP Problem Identification

**Signs of DP Problem:**
- Keywords: "optimal", "maximum", "minimum", "count ways"
- Choices at each step
- Overlapping subproblems
- Optimal substructure property

## Problems Covered

1. Introduction to Dynamic Programming
2. Climbing Stairs
3. Minimum Coin Combination
4. Matrix Pathways
5. Neighborhood Burglary
6. Longest Common Subsequence
7. Longest Palindrome in a String
8. Maximum Subarray Sum
9. 0/1 Knapsack
10. Largest Square in a Matrix

## Interview Tips for Dynamic Programming

💡 **Key Interview Tips:**

1. **Start with brute force** - Understand the problem structure first
2. **Identify subproblems** - What smaller problems need to be solved?
3. **Define state** - What parameters uniquely identify a subproblem?
4. **Find recurrence relation** - How do subproblems relate?
5. **Consider space optimization** - Can you use O(1) or O(n) instead of O(n²)?

### Implementation Examples

**Fibonacci (Classic DP):**
```python
# Memoization (Top-down)
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]

# Tabulation (Bottom-up)
def fibonacci_tab(n):
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

# Space Optimized
def fibonacci_optimized(n):
    if n <= 1:
        return n
    
    prev2, prev1 = 0, 1
    for i in range(2, n + 1):
        current = prev1 + prev2
        prev2, prev1 = prev1, current
    
    return prev1
```

**Longest Common Subsequence:**
```python
def longest_common_subsequence(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]
```

**0/1 Knapsack:**
```python
def knapsack_01(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            # Don't take item i
            dp[i][w] = dp[i-1][w]
            
            # Take item i if possible
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i][w], 
                              dp[i-1][w - weights[i-1]] + values[i-1])
    
    return dp[n][capacity]

# Space optimized version
def knapsack_01_optimized(weights, values, capacity):
    dp = [0] * (capacity + 1)
    
    for i in range(len(weights)):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    
    return dp[capacity]
```

**Maximum Subarray Sum (Kadane's Algorithm):**
```python
def max_subarray_sum(nums):
    max_ending_here = max_so_far = nums[0]
    
    for i in range(1, len(nums)):
        max_ending_here = max(nums[i], max_ending_here + nums[i])
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far
```

**Edit Distance:**
```python
def edit_distance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize base cases
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j],    # delete
                                   dp[i][j-1],    # insert
                                   dp[i-1][j-1])  # replace
    
    return dp[m][n]
```

### Advanced Techniques

**State Compression:**
Reduce space complexity using bitmasks or rolling arrays

**Path Reconstruction:**
Track choices to reconstruct optimal solution

**Multi-dimensional DP:**
Handle problems with multiple state variables

### Common Pitfalls and How to Avoid Them

1. **Wrong Base Cases**
   - Carefully define and implement base cases
   - Test with simple examples

2. **Incorrect State Definition**
   - Ensure state captures all necessary information
   - Avoid redundant state variables

3. **Off-by-One Errors**
   - Be careful with array indices and loop bounds
   - Use clear variable naming

4. **Not Considering All Transitions**
   - Ensure all possible choices are considered
   - Verify recurrence relation is correct

---
*Master dynamic programming to solve complex optimization and counting problems efficiently!*