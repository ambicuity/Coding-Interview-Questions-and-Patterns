# Hash Maps and Sets Pattern

**Author:** Ritesh Rana

## Introduction to Hash Maps and Sets

Hash Maps (also known as Hash Tables or Dictionaries) and Hash Sets are fundamental data structures that provide constant-time average performance for insertions, deletions, and lookups. They are incredibly powerful for solving problems that require fast access to stored data or tracking unique elements.

### Key Concepts

**Hash Map (Dictionary):**
- Stores key-value pairs
- Average O(1) time for insert, delete, and lookup operations
- Keys must be hashable (immutable in Python)
- Perfect for counting, caching, and mapping relationships

**Hash Set:**
- Stores unique elements only
- Average O(1) time for insert, delete, and lookup operations
- Perfect for deduplication and membership testing

### Common Patterns

1. **Frequency Counting** - Count occurrences of elements
2. **Fast Lookups** - Check if element exists in constant time
3. **Complement Finding** - Find pairs that satisfy conditions
4. **Deduplication** - Remove duplicates efficiently
5. **Caching/Memoization** - Store computed results

### When to Use Hash Maps and Sets

**Use Hash Maps when:**
- You need to count occurrences
- You need to map one value to another
- You need fast lookups by key
- You need to group or categorize data

**Use Hash Sets when:**
- You need to track unique elements
- You need fast membership testing
- You want to remove duplicates
- You need set operations (union, intersection)

### Time Complexity Benefits

Most hash map/set operations are **O(1) average case**, which can dramatically improve algorithm efficiency:
- Converting O(n²) nested loops to O(n) single passes
- Replacing O(n log n) sorting with O(n) hash-based solutions

## Interview Tips for Hash Maps and Sets

💡 **Key Interview Tips:**

1. **Think "frequency" and "lookup"** - Most hash problems involve counting or fast access
2. **Consider the complement** - For sum problems, think target - current_value
3. **Use as cache** - Store computed results to avoid recalculation
4. **Handle collisions gracefully** - Understand that O(1) is average case
5. **Choose right data structure** - Map for key-value, Set for uniqueness
6. **Watch memory usage** - Hash structures trade space for time

### Common Hash Map Patterns

```python
# Pattern 1: Frequency counting
frequency = {}
for item in items:
    frequency[item] = frequency.get(item, 0) + 1

# Pattern 2: Complement finding (Two Sum)
seen = {}
for i, num in enumerate(nums):
    complement = target - num
    if complement in seen:
        return [seen[complement], i]
    seen[num] = i

# Pattern 3: Grouping/Categorizing
groups = {}
for item in items:
    key = get_category(item)
    if key not in groups:
        groups[key] = []
    groups[key].append(item)

# Pattern 4: Caching/Memoization
cache = {}
def expensive_function(x):
    if x in cache:
        return cache[x]
    result = compute(x)  # expensive computation
    cache[x] = result
    return result
```

### Common Hash Set Patterns

```python
# Pattern 1: Deduplication
unique_items = set(items)

# Pattern 2: Membership testing
valid_items = {valid1, valid2, valid3}
if item in valid_items:
    process(item)

# Pattern 3: Set operations
set1 = {1, 2, 3}
set2 = {2, 3, 4}
intersection = set1 & set2  # {2, 3}
union = set1 | set2         # {1, 2, 3, 4}
difference = set1 - set2    # {1}
```

## Hash Function and Collision Handling

### Understanding Hash Functions
A hash function converts keys into array indices. Good hash functions:
- Distribute keys uniformly across the array
- Are deterministic (same key always gives same hash)
- Are fast to compute

### Collision Resolution
When two keys hash to the same index:

1. **Chaining** - Store multiple key-value pairs in same slot (using linked lists)
2. **Open Addressing** - Find another empty slot using probing

### Load Factor
- **Load Factor = Number of elements / Array size**
- Keep load factor low (typically < 0.75) for good performance
- Hash tables resize when load factor gets too high

## Language-Specific Implementation Notes

### Python
```python
# Dictionary (Hash Map)
hash_map = {}
hash_map = dict()
hash_map = {'key': 'value'}

# Set (Hash Set)
hash_set = set()
hash_set = {1, 2, 3}

# Counter (specialized hash map for counting)
from collections import Counter
counter = Counter([1, 2, 2, 3])  # {1: 1, 2: 2, 3: 1}

# DefaultDict (hash map with default values)
from collections import defaultdict
dd = defaultdict(list)  # default value is empty list
```

### JavaScript
```javascript
// Map (Hash Map)
const hashMap = new Map();
hashMap.set('key', 'value');

// Object as Hash Map
const obj = {};
obj['key'] = 'value';

// Set (Hash Set)
const hashSet = new Set();
hashSet.add(1);
```

### Java
```java
// HashMap
Map<String, Integer> hashMap = new HashMap<>();
hashMap.put("key", 1);

// HashSet
Set<Integer> hashSet = new HashSet<>();
hashSet.add(1);
```

## Problems Covered

1. [Pair Sum - Unsorted](./pair-sum-unsorted.md) ⭐ (Foundation Problem)
2. [Verify Sudoku Board](./verify-sudoku-board.md)
3. [Zero Striping](./zero-striping.md)
4. [Longest Chain of Consecutive Numbers](./longest-consecutive-sequence.md)
5. [Geometric Sequence Triplets](./geometric-sequence-triplets.md)

## Performance Comparison: Hash vs Array vs Sorting

| Operation | Array/List | Sorted Array | Hash Map/Set |
|-----------|------------|--------------|--------------|
| Insert | O(1) end, O(n) middle | O(n) | O(1) average |
| Delete | O(n) | O(n) | O(1) average |
| Search | O(n) | O(log n) | O(1) average |
| Space | O(n) | O(n) | O(n) |

## Common Pitfalls and How to Avoid Them

❌ **Don't assume O(1) is guaranteed** - It's average case, worst case can be O(n)
❌ **Don't use mutable objects as keys** - They can't be hashed consistently
❌ **Don't ignore memory overhead** - Hash tables use extra space for efficiency
❌ **Don't forget about hash collisions** - They can degrade performance
❌ **Don't use hash when order matters** - Use OrderedDict/LinkedHashMap if needed

✅ **Do choose appropriate data structure** - Map for key-value, Set for uniqueness
✅ **Do handle edge cases** - Empty inputs, single elements, all duplicates
✅ **Do consider alternative approaches** - Sometimes sorting might be better
✅ **Do understand language-specific behaviors** - Each language has nuances

---
*Hash Maps and Sets are your best friends for optimization - master them to solve problems elegantly!*