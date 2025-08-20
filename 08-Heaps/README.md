# Heaps Pattern

**Author:** Ritesh Rana

## Introduction to Heaps

A Heap is a specialized tree-based data structure that satisfies the heap property. In a max heap, the parent node is always greater than or equal to its children, while in a min heap, the parent node is always smaller than or equal to its children. Heaps are commonly implemented as binary heaps using arrays and are fundamental for priority-based algorithms.

### Key Concepts

**Heap Properties:**
- **Complete Binary Tree**: All levels are filled except possibly the last level
- **Heap Property**: Parent-child relationship follows min or max constraint
- **Array Implementation**: Efficient representation using arrays
- **Root Access**: Minimum (min heap) or maximum (max heap) element at root

**Types of Heaps:**
1. **Min Heap**: Parent ≤ Children (smallest element at root)
2. **Max Heap**: Parent ≥ Children (largest element at root)
3. **Binary Heap**: Each parent has at most 2 children
4. **D-ary Heap**: Each parent has at most d children

### Common Patterns

1. **Priority Queue** - Processing elements by priority
2. **Top K Elements** - Finding k largest or smallest elements
3. **Median Finding** - Using two heaps to track median
4. **Merge K Lists** - Efficiently merging multiple sorted lists
5. **Scheduling** - Task scheduling based on priority
6. **Graph Algorithms** - Dijkstra's algorithm, Prim's MST

### When to Use Heaps

- Need quick access to min/max element
- Implementing priority queues
- Finding top K elements
- Streaming data with priorities
- Graph algorithms requiring priority processing
- Median tracking in data streams

### Time and Space Complexity

| Operation | Time Complexity |
|-----------|----------------|
| Insert | O(log n) |
| Extract Min/Max | O(log n) |
| Peek Min/Max | O(1) |
| Delete | O(log n) |
| Build Heap | O(n) |

**Space Complexity:** O(n)

## Problems Covered

1. Introduction to Heaps
2. K Most Frequent Strings
3. Combine Sorted Linked Lists
4. Median of an Integer Stream
5. Sort a K-Sorted Array

## Interview Tips for Heaps

💡 **Key Interview Tips:**

1. **Choose heap type** - Min heap for smallest elements, max heap for largest
2. **Consider two heaps** - For problems like finding median
3. **Think priority** - If problem involves processing by priority, consider heaps
4. **Array indices** - For array implementation: parent = (i-1)//2, children = 2*i+1, 2*i+2
5. **Custom comparators** - Define custom comparison for complex objects

### Implementation Examples

**Min Heap Operations (Python):**
```python
import heapq

# Min heap operations
heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 4)

min_element = heapq.heappop(heap)  # Returns 1
peek = heap[0]  # Peek at minimum without removing
```

**Max Heap (Python - using negation):**
```python
import heapq

max_heap = []
heapq.heappush(max_heap, -3)  # Negate for max heap
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -4)

max_element = -heapq.heappop(max_heap)  # Returns 4
```

**Finding Median using Two Heaps:**
```python
class MedianFinder:
    def __init__(self):
        self.max_heap = []  # For smaller half
        self.min_heap = []  # For larger half
    
    def add_number(self, num):
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        
        # Balance heaps
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        elif len(self.min_heap) > len(self.max_heap) + 1:
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)
    
    def find_median(self):
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        elif len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return self.min_heap[0]
```

### Common Pitfalls and How to Avoid Them

1. **Heap Type Confusion**
   - Remember: Python heapq is min heap by default
   - Use negation trick for max heap functionality

2. **Index Calculations**
   - Parent: (i-1)//2, Left child: 2*i+1, Right child: 2*i+2
   - Be careful with 0-based indexing

3. **Balancing Two Heaps**
   - Maintain size difference ≤ 1 for median problems
   - Always rebalance after insertions

---
*Master heap operations to efficiently solve priority-based and top-K problems!*