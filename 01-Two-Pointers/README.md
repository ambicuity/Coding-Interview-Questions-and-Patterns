# Two Pointers Pattern

**Author:** Ritesh Rana

## Introduction to Two Pointers

The Two Pointers technique is a powerful algorithmic pattern that uses two pointers to traverse data structures, typically arrays or strings, to solve problems efficiently. This approach is particularly useful when you need to find pairs or triplets of elements that satisfy certain conditions.

### Key Concepts

The two-pointer technique involves:
1. **Initialization**: Set two pointers at specific positions (usually start and end, or both at start)
2. **Movement**: Move pointers based on certain conditions
3. **Termination**: Continue until pointers meet or cross

### Common Patterns

1. **Opposite Direction**: Start from both ends and move towards center
2. **Same Direction**: Both pointers start from the same side and move at different speeds
3. **Fast and Slow**: One pointer moves faster than the other

### When to Use Two Pointers

- Finding pairs in sorted arrays
- Palindrome problems
- Removing duplicates
- Merging sorted arrays
- Container problems (area, volume calculations)

### Time Complexity Benefits

Two pointers often reduce time complexity from O(n²) to O(n) by eliminating the need for nested loops.

## Interview Tips for Two Pointers

💡 **Key Interview Tips:**

1. **Always ask if the array is sorted** - Many two-pointer problems require sorted input
2. **Consider sorting first** - If not sorted, sorting might enable two-pointer approach
3. **Handle edge cases** - Empty arrays, single elements, duplicate values
4. **Think about pointer movement** - When to move left, right, or both
5. **Watch for infinite loops** - Ensure pointers always make progress
6. **Consider multiple passes** - Sometimes you need to fix one element and use two pointers on the rest

## Problems Covered

1. [Pair Sum - Sorted](./pair-sum-sorted.md) ⭐ (Foundation Problem)
2. [Triplet Sum](./triplet-sum.md) ⭐ (Detailed Example)
3. [Valid Palindrome](./valid-palindrome.md) ⭐ (Complete Implementation)
4. [Container With Most Water](./container-with-most-water.md) ⭐ (Complete Implementation)
5. [Shift Zeros to the End](./shift-zeros-to-end.md)
6. [Next Lexicographical Sequence](./next-lexicographical-sequence.md)

---
*Master the two pointers technique to solve array and string problems efficiently!*