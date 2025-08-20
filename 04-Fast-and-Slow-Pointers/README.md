# Fast and Slow Pointers Pattern

**Author:** Ritesh Rana

## Introduction to Fast and Slow Pointers

The Fast and Slow Pointers technique, also known as Floyd's Tortoise and Hare algorithm, is a powerful two-pointer approach where one pointer moves faster than the other. This technique is particularly useful for solving problems involving cycles in linked lists and finding specific positions without knowing the length of the data structure.

### Key Concepts

**Basic Principle:**
- **Slow Pointer**: Moves one step at a time
- **Fast Pointer**: Moves two steps at a time
- **Meeting Point**: When fast and slow pointers meet, it indicates a cycle
- **Cycle Detection**: If fast pointer reaches null, no cycle exists

**Common Speed Ratios:**
1. **1:2 Ratio** - Most common (slow moves 1, fast moves 2)
2. **1:3 Ratio** - Less common but useful in specific cases
3. **Variable Speed** - Speed changes based on conditions

### Common Patterns

1. **Cycle Detection** - Detecting loops in linked lists
2. **Finding Middle** - Locating the middle element
3. **Cycle Length** - Calculating the length of a cycle
4. **Cycle Start** - Finding where the cycle begins
5. **Happy Numbers** - Detecting cycles in number sequences

### When to Use Fast and Slow Pointers

- Detecting cycles in linked lists
- Finding the middle of a linked list
- Detecting patterns in sequences
- Memory-efficient solutions (O(1) space)
- Problems involving "meeting points"

### Time and Space Complexity

**Time Complexity:** O(n) - Each element visited at most twice
**Space Complexity:** O(1) - Only using two pointers

## Problems Covered

1. Introduction to Fast and Slow Pointers
2. Linked List Loop
3. Linked List Midpoint  
4. Happy Number

## Interview Tips for Fast and Slow Pointers

💡 **Key Interview Tips:**

1. **Visualize pointer movement** - Draw diagrams to understand how pointers traverse the structure
2. **Master the mathematical proof** - Understand why fast/slow pointers guarantee cycle detection
3. **Handle edge cases systematically** - Empty lists, single nodes, self-loops, no cycles
4. **Choose appropriate speed ratios** - Usually 1:2, but consider problem requirements
5. **Practice state management** - Track what information is available at each step
6. **Understand termination conditions** - Know when to stop and what the result means
7. **Apply to various domains** - Linked lists, arrays, number sequences, graphs

### Comprehensive Implementation Patterns

**1. Cycle Detection Template:**
```python
def detect_cycle_template(head):
    """Template for cycle detection in linked list"""
    if not head or not head.next:
        return False
    
    slow = fast = head
    
    # Phase 1: Detect if cycle exists
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True  # Cycle detected
    
    return False  # No cycle

# Robust implementation with detailed checking
def has_cycle_robust(head):
    """Cycle detection with comprehensive error handling"""
    if not head:
        return False
    
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    
    return False

# Alternative: Start with different positions
def has_cycle_alternative(head):
    """Alternative starting positions"""
    if not head or not head.next:
        return False
    
    slow = head
    fast = head.next  # Start fast one step ahead
    
    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next
    
    return True
```

**2. Finding Cycle Start (Floyd's Algorithm Complete):**
```python
def find_cycle_start(head):
    """Find the starting node of cycle using Floyd's algorithm"""
    if not head or not head.next:
        return None
    
    # Phase 1: Detect cycle
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            break
    else:
        return None  # No cycle found
    
    # Phase 2: Find cycle start
    # Reset one pointer to head, move both at same speed
    start = head
    while start != slow:
        start = start.next
        slow = slow.next
    
    return start  # This is where cycle begins

def find_cycle_length(head):
    """Find the length of the cycle"""
    cycle_start = find_cycle_start(head)
    if not cycle_start:
        return 0
    
    current = cycle_start.next
    length = 1
    
    while current != cycle_start:
        current = current.next
        length += 1
    
    return length

def analyze_cycle_complete(head):
    """Complete cycle analysis"""
    if not head:
        return {"has_cycle": False}
    
    # Detect cycle and find meeting point
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            # Cycle detected, find start
            start = head
            while start != slow:
                start = start.next
                slow = slow.next
            
            # Find cycle length
            current = start.next
            length = 1
            while current != start:
                current = current.next
                length += 1
            
            return {
                "has_cycle": True,
                "cycle_start": start,
                "cycle_length": length
            }
    
    return {"has_cycle": False}
```

**3. Finding Middle Element:**
```python
def find_middle(head):
    """Find middle element of linked list"""
    if not head:
        return None
    
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow  # Middle element

def find_middle_variations(head):
    """Different middle-finding variations"""
    if not head:
        return None
    
    # Variation 1: For even length, return first middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
    
def find_middle_and_length(head):
    """Find both middle and total length"""
    if not head:
        return None, 0
    
    slow = fast = head
    length = 0
    
    while fast:
        length += 1
        slow = slow.next if fast.next else slow
        fast = fast.next.next if fast.next else None
    
    return slow, length

def split_list_at_middle(head):
    """Split linked list into two halves"""
    if not head or not head.next:
        return head, None
    
    slow = fast = head
    prev = None
    
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    
    # Break the connection
    if prev:
        prev.next = None
    
    return head, slow  # First half, second half
```

**4. Advanced Applications:**
```python
def is_happy_number(n):
    """Check if number is happy using cycle detection"""
    def get_sum_of_squares(num):
        total = 0
        while num > 0:
            digit = num % 10
            total += digit * digit
            num //= 10
        return total
    
    slow = fast = n
    
    while True:
        slow = get_sum_of_squares(slow)
        fast = get_sum_of_squares(get_sum_of_squares(fast))
        
        if fast == 1:
            return True
        if slow == fast:
            return False  # Cycle detected, not happy

def find_duplicate_number(nums):
    """Find duplicate in array using Floyd's algorithm"""
    # Phase 1: Find meeting point
    slow = fast = nums[0]
    
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    
    # Phase 2: Find entrance to cycle (duplicate)
    start = nums[0]
    while start != slow:
        start = nums[start]
        slow = nums[slow]
    
    return start

def remove_cycle(head):
    """Remove cycle from linked list"""
    if not head or not head.next:
        return head
    
    # Find meeting point
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return head  # No cycle
    
    # Find cycle start
    start = head
    while start.next != slow.next:
        start = start.next
        slow = slow.next
    
    # Break the cycle
    slow.next = None
    return head

def palindrome_linked_list(head):
    """Check if linked list is palindrome using fast/slow pointers"""
    if not head or not head.next:
        return True
    
    # Find middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Reverse second half
    def reverse_list(node):
        prev = None
        while node:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
        return prev
    
    second_half = reverse_list(slow)
    
    # Compare first and second half
    first_half = head
    while second_half:
        if first_half.val != second_half.val:
            return False
        first_half = first_half.next
        second_half = second_half.next
    
    return True
```

**5. Array and Sequence Applications:**
```python
def find_duplicate_in_array_cycle(nums):
    """Find duplicate using array as linked list"""
    # Each number points to index (creating implicit linked list)
    slow = fast = nums[0]
    
    # Find meeting point
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    
    # Find cycle start (duplicate number)
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return slow

def circular_array_loop(nums):
    """Check if circular array has a loop"""
    def get_next_index(i):
        return (i + nums[i]) % len(nums)
    
    for i in range(len(nums)):
        if nums[i] == 0:
            continue
        
        slow = fast = i
        
        # Check if all elements in cycle have same direction
        while (nums[slow] > 0) == (nums[get_next_index(slow)] > 0) and \
              (nums[fast] > 0) == (nums[get_next_index(fast)] > 0) and \
              (nums[fast] > 0) == (nums[get_next_index(get_next_index(fast))] > 0):
            
            slow = get_next_index(slow)
            fast = get_next_index(get_next_index(fast))
            
            if slow == fast:
                # Check if cycle length > 1
                if slow == get_next_index(slow):
                    break
                return True
        
        # Mark visited elements as 0
        val = nums[i]
        while nums[i] != 0 and (nums[i] > 0) == (val > 0):
            next_i = get_next_index(i)
            nums[i] = 0
            i = next_i
    
    return False
```

### Mathematical Foundation and Proof

**Why Fast and Slow Pointers Work:**

1. **No Cycle Case**: Fast pointer reaches end first
2. **With Cycle Case**: Fast pointer eventually catches slow pointer

**Proof for Cycle Detection:**
- Let cycle start at position μ and have length λ
- When slow enters cycle, fast is at most λ-1 positions ahead
- Fast gains 1 position per iteration on slow
- They will meet within λ iterations

**Finding Cycle Start Proof:**
- Meeting point is μ + k positions from cycle start
- Distance from head to cycle start = distance from meeting point to cycle start
- Moving both pointers at same speed ensures they meet at cycle start

### Advanced Patterns and Optimizations

**1. Multi-Speed Pointers:**
```python
def three_speed_detection(head):
    """Using three different speeds for complex detection"""
    if not head:
        return False
    
    slow = medium = fast = head
    
    while fast and fast.next and fast.next.next:
        slow = slow.next
        medium = medium.next.next
        fast = fast.next.next.next
        
        if slow == medium or slow == fast or medium == fast:
            return True
    
    return False
```

**2. Bidirectional Fast-Slow:**
```python
def bidirectional_middle_search(arr, target):
    """Search from both ends with different speeds"""
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        if arr[left] == target:
            return left
        if arr[right] == target:
            return right
        
        left += 1
        right -= 2  # Different speed
        
        if left <= right and arr[left] == target:
            return left
    
    return -1
```

### Common Pitfalls and Expert Solutions

1. **Null Pointer Errors:**
   ```python
   # ❌ Wrong: Not checking fast.next
   while fast:
       slow = slow.next
       fast = fast.next.next  # Error if fast.next is null
   
   # ✅ Correct: Proper null checking
   while fast and fast.next:
       slow = slow.next
       fast = fast.next.next
   ```

2. **Initialization Mistakes:**
   ```python
   # ❌ Wrong: Starting positions might miss cycles
   slow = head
   fast = head
   if slow == fast:  # Always true initially!
       return True
   
   # ✅ Correct: Move before first comparison
   slow = head
   fast = head
   while fast and fast.next:
       slow = slow.next
       fast = fast.next.next
       if slow == fast:  # Now meaningful comparison
           return True
   ```

3. **Edge Case Oversight:**
   ```python
   # ❌ Wrong: Not handling single node or empty list
   def find_middle(head):
       slow = fast = head
       while fast.next:  # Error on single node
           slow = slow.next
           fast = fast.next.next
       return slow
   
   # ✅ Correct: Comprehensive edge case handling
   def find_middle(head):
       if not head:
           return None
       
       slow = fast = head
       while fast and fast.next:
           slow = slow.next
           fast = fast.next.next
       return slow
   ```

### Testing and Performance Analysis

**Test Framework:**
```python
def test_fast_slow_algorithms():
    """Comprehensive test suite"""
    
    # Create test linked lists
    def create_list_with_cycle(values, cycle_start_idx):
        if not values:
            return None
        
        nodes = [ListNode(val) for val in values]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        
        if cycle_start_idx >= 0:
            nodes[-1].next = nodes[cycle_start_idx]
        
        return nodes[0]
    
    test_cases = [
        # (values, cycle_start, expected_has_cycle, expected_middle_val)
        ([1, 2, 3, 4, 5], -1, False, 3),  # No cycle, odd length
        ([1, 2, 3, 4], -1, False, 3),     # No cycle, even length
        ([1, 2, 3, 4, 5], 2, True, None),  # Cycle starting at index 2
        ([1], -1, False, 1),               # Single node
        ([], -1, False, None),             # Empty list
    ]
    
    for values, cycle_start, expected_cycle, expected_middle in test_cases:
        head = create_list_with_cycle(values, cycle_start)
        
        # Test cycle detection
        has_cycle = detect_cycle_template(head)
        cycle_status = "PASS" if has_cycle == expected_cycle else "FAIL"
        
        # Test middle finding (only for non-cyclic lists)
        if not expected_cycle and head:
            middle = find_middle(head)
            middle_val = middle.val if middle else None
            middle_status = "PASS" if middle_val == expected_middle else "FAIL"
        else:
            middle_status = "N/A"
        
        print(f"Values: {values}, Cycle: {cycle_status}, Middle: {middle_status}")

def benchmark_performance():
    """Performance analysis of fast-slow vs alternatives"""
    import time
    
    # Compare against naive approaches
    sizes = [1000, 10000, 100000]
    
    for size in sizes:
        # Create large linked list
        head = ListNode(0)
        current = head
        for i in range(1, size):
            current.next = ListNode(i)
            current = current.next
        
        # Add cycle at middle
        middle_node = head
        for _ in range(size // 2):
            middle_node = middle_node.next
        current.next = middle_node
        
        # Benchmark fast-slow algorithm
        start_time = time.time()
        has_cycle_robust(head)
        fast_slow_time = time.time() - start_time
        
        print(f"Size {size}: Fast-Slow = {fast_slow_time:.6f}s")
```

---
*Master the fast and slow pointers technique for elegant cycle detection and middle-finding solutions!*