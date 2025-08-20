# Backtracking Pattern

**Author:** Ritesh Rana

## Introduction to Backtracking

Backtracking is a algorithmic technique for solving problems by building solutions incrementally and abandoning partial solutions that cannot lead to a valid complete solution. It systematically explores all possible paths and "backtracks" when a dead end is reached, making it ideal for constraint satisfaction problems.

### Key Concepts

**Basic Principle:**
- **Incremental Building**: Construct solution step by step
- **Constraint Checking**: Validate partial solutions early
- **Backtrack**: Undo choices that lead to invalid solutions
- **Exhaustive Search**: Explore all valid possibilities
- **Pruning**: Eliminate branches that cannot lead to solutions

**Backtracking Template:**
1. Choose an option
2. Check if choice is valid
3. Make the choice (modify state)
4. Recursively solve subproblem
5. Undo the choice (backtrack)

### Common Patterns

1. **Permutations** - Generate all arrangements
2. **Combinations** - Generate all selections
3. **Subset Generation** - All possible subsets
4. **N-Queens** - Constraint satisfaction problems
5. **Sudoku Solving** - Fill grid with constraints
6. **Path Finding** - All paths between points
7. **Word Search** - Finding words in grids

### When to Use Backtracking

- Generate all possible solutions
- Constraint satisfaction problems
- Optimization problems (with pruning)
- Combinatorial problems
- Game playing (chess, sudoku)
- Puzzle solving

### Time and Space Complexity

**Time Complexity:** Often exponential O(b^d) where b is branching factor, d is depth
**Space Complexity:** O(d) for recursion stack plus solution space

Pruning can significantly improve performance in practice.

## Problems Covered

1. Introduction to Backtracking
2. Find All Permutations
3. Find All Subsets
4. N Queens
5. Combinations of a Sum
6. Phone Keypad Combinations

## Interview Tips for Backtracking

💡 **Key Interview Tips:**

1. **Identify the choices** - What decisions can be made at each step?
2. **Define constraints** - What makes a choice valid or invalid?
3. **Early termination** - Prune branches that cannot succeed
4. **State management** - Carefully handle making/undoing choices
5. **Base case** - When is a complete solution found?

### Implementation Examples

**Generate All Permutations:**
```python
def permutations(nums):
    result = []
    
    def backtrack(current_permutation):
        # Base case: permutation is complete
        if len(current_permutation) == len(nums):
            result.append(current_permutation[:])  # Make a copy
            return
        
        # Try each unused number
        for num in nums:
            if num not in current_permutation:
                # Make choice
                current_permutation.append(num)
                
                # Recursively build rest of permutation
                backtrack(current_permutation)
                
                # Undo choice (backtrack)
                current_permutation.pop()
    
    backtrack([])
    return result
```

**Generate All Subsets:**
```python
def subsets(nums):
    result = []
    
    def backtrack(start, current_subset):
        # Add current subset to result
        result.append(current_subset[:])
        
        # Try adding each remaining element
        for i in range(start, len(nums)):
            # Include nums[i]
            current_subset.append(nums[i])
            
            # Recursively generate subsets
            backtrack(i + 1, current_subset)
            
            # Exclude nums[i] (backtrack)
            current_subset.pop()
    
    backtrack(0, [])
    return result
```

**N-Queens Problem:**
```python
def solve_n_queens(n):
    result = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    
    def is_safe(row, col):
        # Check column
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        
        # Check diagonal (top-left to bottom-right)
        for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
            if board[i][j] == 'Q':
                return False
        
        # Check anti-diagonal (top-right to bottom-left)
        for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
            if board[i][j] == 'Q':
                return False
        
        return True
    
    def backtrack(row):
        if row == n:
            # Found valid solution
            result.append([''.join(row) for row in board])
            return
        
        for col in range(n):
            if is_safe(row, col):
                # Place queen
                board[row][col] = 'Q'
                
                # Recursively place queens in next rows
                backtrack(row + 1)
                
                # Remove queen (backtrack)
                board[row][col] = '.'
    
    backtrack(0)
    return result
```

**Combination Sum:**
```python
def combination_sum(candidates, target):
    result = []
    
    def backtrack(start, current_combination, remaining):
        if remaining == 0:
            result.append(current_combination[:])
            return
        
        for i in range(start, len(candidates)):
            num = candidates[i]
            if num <= remaining:
                # Include this number
                current_combination.append(num)
                
                # Recursively find combinations
                # Can reuse same number (i, not i+1)
                backtrack(i, current_combination, remaining - num)
                
                # Backtrack
                current_combination.pop()
    
    backtrack(0, [], target)
    return result
```

### Optimization Techniques

**Pruning:**
- Early termination when partial solution cannot succeed
- Sort input to enable better pruning
- Use constraints to avoid invalid branches

**Memoization:**
- Cache results for overlapping subproblems
- Combine with dynamic programming when applicable

### Common Pitfalls and How to Avoid Them

1. **Forgetting to Backtrack**
   - Always undo changes before returning
   - Use clear make/unmake choice pattern

2. **Modifying Shared State**
   - Be careful with mutable objects
   - Make copies when adding to result

3. **Inefficient Pruning**
   - Add constraint checks as early as possible
   - Sort inputs when beneficial

4. **Stack Overflow**
   - Consider depth limits for deep recursion
   - Use iterative approaches for very large inputs

---
*Master backtracking to solve complex combinatorial and constraint satisfaction problems!*