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

1. **Choose the right heap type** - Min heap for smallest elements, max heap for largest
2. **Two heaps pattern** - Powerful for problems like finding median, percentiles
3. **Priority-based problems** - If problem involves processing by priority, consider heaps
4. **Array representation** - For array implementation: parent = (i-1)//2, children = 2*i+1, 2*i+2
5. **Custom comparators** - Define custom comparison functions for complex objects
6. **Time complexity awareness** - Heaps are O(log n) for most operations, not O(1)
7. **Space efficiency** - Heaps provide good balance between time and space complexity

### Comprehensive Heap Implementation Examples

**1. Manual Min Heap Implementation:**
```python
class MinHeap:
    def __init__(self):
        self.heap = []
    
    def parent(self, i):
        return (i - 1) // 2
    
    def left_child(self, i):
        return 2 * i + 1
    
    def right_child(self, i):
        return 2 * i + 2
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)
    
    def extract_min(self):
        if not self.heap:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        
        return root
    
    def _heapify_up(self, i):
        parent = self.parent(i)
        if i > 0 and self.heap[i] < self.heap[parent]:
            self.swap(i, parent)
            self._heapify_up(parent)
    
    def _heapify_down(self, i):
        min_idx = i
        left = self.left_child(i)
        right = self.right_child(i)
        
        if left < len(self.heap) and self.heap[left] < self.heap[min_idx]:
            min_idx = left
        
        if right < len(self.heap) and self.heap[right] < self.heap[min_idx]:
            min_idx = right
        
        if min_idx != i:
            self.swap(i, min_idx)
            self._heapify_down(min_idx)
    
    def peek(self):
        return self.heap[0] if self.heap else None
    
    def size(self):
        return len(self.heap)
```

**2. Advanced Heap Usage Patterns:**

```python
import heapq
from collections import defaultdict

# Top K Frequent Elements
def top_k_frequent(nums, k):
    count = defaultdict(int)
    for num in nums:
        count[num] += 1
    
    # Use min heap to keep only top k elements
    heap = []
    for num, freq in count.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)
    
    return [num for freq, num in heap]

# Kth Largest Element in Stream
class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        
        # Keep only k largest elements
        while len(self.heap) > k:
            heapq.heappop(self.heap)
    
    def add(self, val):
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]

# Merge K Sorted Lists
def merge_k_lists(lists):
    heap = []
    
    # Initialize heap with first element from each list
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst.val, i, lst))
    
    dummy = ListNode(0)
    current = dummy
    
    while heap:
        val, i, node = heapq.heappop(heap)
        current.next = ListNode(val)
        current = current.next
        
        # Add next node from the same list
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    
    return dummy.next

# Task Scheduler with Cooling Time
def least_interval(tasks, n):
    count = defaultdict(int)
    for task in tasks:
        count[task] += 1
    
    # Max heap for frequencies
    heap = [-freq for freq in count.values()]
    heapq.heapify(heap)
    
    time = 0
    queue = []  # (remaining_freq, available_time)
    
    while heap or queue:
        time += 1
        
        if heap:
            freq = heapq.heappop(heap)
            if freq < -1:  # Still has remaining tasks
                queue.append((freq + 1, time + n))
        
        # Check if any task becomes available
        if queue and queue[0][1] == time:
            heapq.heappush(heap, queue.pop(0)[0])
    
    return time
```

**3. Custom Comparators and Complex Objects:**

```python
from dataclasses import dataclass
from typing import Any

@dataclass
class Task:
    id: int
    priority: int
    deadline: int
    
    def __lt__(self, other):
        # Higher priority first, then earlier deadline
        if self.priority != other.priority:
            return self.priority > other.priority
        return self.deadline < other.deadline

# Using custom objects in heap
def schedule_tasks(tasks):
    heap = []
    for task in tasks:
        heapq.heappush(heap, task)
    
    scheduled = []
    while heap:
        task = heapq.heappop(heap)
        scheduled.append(task)
    
    return scheduled

# Alternative: Using tuples for custom comparison
def dijkstra_shortest_path(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # (distance, node)
    pq = [(0, start)]
    visited = set()
    
    while pq:
        current_dist, u = heapq.heappop(pq)
        
        if u in visited:
            continue
        
        visited.add(u)
        
        for v, weight in graph[u].items():
            distance = current_dist + weight
            
            if distance < distances[v]:
                distances[v] = distance
                heapq.heappush(pq, (distance, v))
    
    return distances
```

**4. Advanced Two-Heap Patterns:**

```python
class RunningMedian:
    def __init__(self):
        self.max_heap = []  # Smaller half (max heap)
        self.min_heap = []  # Larger half (min heap)
    
    def add_number(self, num):
        # Always add to max_heap first
        heapq.heappush(self.max_heap, -num)
        
        # Move the largest from max_heap to min_heap
        val = -heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, val)
        
        # Balance if min_heap becomes larger
        if len(self.min_heap) > len(self.max_heap):
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)
    
    def find_median(self):
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return (-self.max_heap[0] + self.min_heap[0]) / 2.0

# Sliding Window Median
def median_sliding_window(nums, k):
    def get_median(window):
        sorted_window = sorted(window)
        mid = len(sorted_window) // 2
        if k % 2 == 1:
            return float(sorted_window[mid])
        return (sorted_window[mid-1] + sorted_window[mid]) / 2.0
    
    result = []
    window = []
    
    for i in range(len(nums)):
        window.append(nums[i])
        
        if len(window) > k:
            window.remove(nums[i - k])
        
        if len(window) == k:
            result.append(get_median(window))
    
    return result
```

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

### Heap Optimization Techniques and Advanced Topics

**1. Build Heap Optimization (O(n) construction):**
```python
def build_min_heap(arr):
    """Build heap in O(n) time instead of O(n log n)"""
    n = len(arr)
    
    # Start from last non-leaf node and heapify down
    for i in range(n // 2 - 1, -1, -1):
        heapify_down(arr, i, n)
    
    return arr

def heapify_down(arr, i, heap_size):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < heap_size and arr[left] < arr[smallest]:
        smallest = left
    
    if right < heap_size and arr[right] < arr[smallest]:
        smallest = right
    
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify_down(arr, smallest, heap_size)
```

**2. Heap Sort Implementation:**
```python
def heap_sort(arr):
    """Sort array using heap sort - O(n log n) time, O(1) space"""
    n = len(arr)
    
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify_down_max(arr, i, n)
    
    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Move current root to end
        heapify_down_max(arr, 0, i)  # Restore heap property
    
    return arr

def heapify_down_max(arr, i, heap_size):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < heap_size and arr[left] > arr[largest]:
        largest = left
    
    if right < heap_size and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify_down_max(arr, largest, heap_size)
```

**3. D-ary Heap (More than 2 children per node):**
```python
class DaryHeap:
    def __init__(self, d=2):
        self.d = d  # Number of children per node
        self.heap = []
    
    def parent(self, i):
        return (i - 1) // self.d
    
    def children(self, i):
        return [self.d * i + j for j in range(1, self.d + 1)]
    
    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)
    
    def _heapify_up(self, i):
        if i == 0:
            return
        
        parent = self.parent(i)
        if self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            self._heapify_up(parent)
```

### Problem-Solving Strategies with Heaps

**When to Use Heaps:**

| Problem Pattern | Heap Type | Complexity | Example |
|-----------------|-----------|------------|---------|
| Find top K elements | Min heap of size K | O(n log k) | Top K frequent elements |
| Streaming median | Two heaps | O(log n) per insert | Running median |
| Merge K sorted | Min heap | O(n log k) | Merge K sorted arrays |
| Shortest path | Min heap | O((V+E) log V) | Dijkstra's algorithm |
| Task scheduling | Priority heap | O(n log n) | CPU scheduling |

**Common Heap Patterns:**

1. **Top K Pattern**: Use min heap to keep smallest K elements
2. **Two Heaps Pattern**: Split data into two parts for median-like problems
3. **Priority Processing**: Process elements by priority using max/min heap
4. **Merge Pattern**: Efficiently merge multiple sorted sequences

### Performance Analysis and Benchmarking

**Time Complexity Summary:**
- **Build Heap**: O(n) using bottom-up approach
- **Insert/Delete**: O(log n) for maintaining heap property
- **Peek**: O(1) for accessing root element
- **Heap Sort**: O(n log n) time, O(1) space

**Space Complexity:**
- **Array Implementation**: O(n) for n elements
- **Pointer Implementation**: O(n) + overhead for pointers

**Benchmark Comparison:**
```python
import time
import heapq
import random

def benchmark_heap_operations():
    sizes = [1000, 10000, 100000]
    
    for size in sizes:
        # Generate random data
        data = [random.randint(1, 1000000) for _ in range(size)]
        
        # Benchmark heapify
        start_time = time.time()
        heap = data.copy()
        heapq.heapify(heap)
        heapify_time = time.time() - start_time
        
        # Benchmark insertion
        start_time = time.time()
        heap2 = []
        for item in data:
            heapq.heappush(heap2, item)
        insert_time = time.time() - start_time
        
        print(f"Size {size}:")
        print(f"  Heapify: {heapify_time:.4f}s")
        print(f"  Insert: {insert_time:.4f}s")
        print(f"  Ratio: {insert_time/heapify_time:.2f}x")
```

### Common Pitfalls and Solutions

1. **Heap Type Confusion**
   - **Problem**: Using max heap when min heap needed
   - **Solution**: Clearly understand what you need at the root
   - **Python Tip**: Use `-value` for max heap with heapq

2. **Index Calculation Errors**
   - **Problem**: Wrong parent/child calculations
   - **Solution**: Remember 0-based indexing formulas
   - **Check**: parent=(i-1)//2, left=2*i+1, right=2*i+2

3. **Balancing Issues in Two-Heap Pattern**
   - **Problem**: Incorrect size maintenance
   - **Solution**: Always maintain size difference ≤ 1
   - **Pattern**: Add to one heap, then balance

4. **Mutating Objects in Heap**
   - **Problem**: Changing priority after insertion breaks heap property
   - **Solution**: Remove and re-insert, or use decrease-key operation

5. **Memory Usage with Large Heaps**
   - **Problem**: Running out of memory with large datasets
   - **Solution**: Consider external sorting or streaming algorithms

### Testing and Validation

**Heap Property Validation:**
```python
def validate_min_heap(heap):
    """Validate that array maintains min heap property"""
    for i in range(len(heap)):
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < len(heap) and heap[i] > heap[left]:
            return False, f"Violation at index {i} and {left}"
        
        if right < len(heap) and heap[i] > heap[right]:
            return False, f"Violation at index {i} and {right}"
    
    return True, "Heap property maintained"

# Test suite for heap operations
def test_heap_operations():
    test_cases = [
        [],  # Empty heap
        [1],  # Single element
        [1, 2, 3, 4, 5],  # Ascending
        [5, 4, 3, 2, 1],  # Descending
        [3, 1, 4, 1, 5, 9, 2, 6]  # Random
    ]
    
    for i, case in enumerate(test_cases):
        print(f"Test case {i}: {case}")
        heap = case.copy()
        heapq.heapify(heap)
        is_valid, message = validate_min_heap(heap)
        print(f"  Result: {heap}")
        print(f"  Valid: {message}")
```

---
*Master heap operations to efficiently solve priority-based, top-K, and streaming data problems!*