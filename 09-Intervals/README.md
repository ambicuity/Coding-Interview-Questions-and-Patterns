# Intervals Pattern

**Author:** Ritesh Rana

## Introduction to Intervals

Intervals represent ranges of values defined by start and end points. Interval problems are common in scheduling, calendar applications, and range-based queries. These problems often involve merging overlapping intervals, finding intersections, or determining optimal scheduling solutions.

### Key Concepts

**Interval Representation:**
- **Start Time**: Beginning of the interval
- **End Time**: End of the interval  
- **Open vs Closed**: Whether endpoints are included
- **Overlap**: When intervals share common points

**Common Operations:**
1. **Merge**: Combine overlapping intervals
2. **Insert**: Add new interval and merge if necessary
3. **Intersection**: Find common parts between intervals
4. **Union**: Combine all intervals covering the range
5. **Gap Finding**: Identify spaces between intervals

### Common Patterns

1. **Merge Overlapping Intervals** - Combining intersecting ranges
2. **Insert Interval** - Adding new interval to sorted list
3. **Interval Intersection** - Finding overlaps between interval lists
4. **Meeting Rooms** - Scheduling and resource allocation
5. **Range Queries** - Answering queries over ranges
6. **Event Scheduling** - Optimal scheduling problems

### When to Use Intervals

- Scheduling and calendar problems
- Range-based queries
- Resource allocation
- Time-based event processing
- Geometric problems involving ranges
- Optimization problems with time constraints

### Key Algorithms

**Sorting Strategy:**
Most interval problems benefit from sorting by start time (or end time)

**Overlap Detection:**
Two intervals [a, b] and [c, d] overlap if: max(a, c) < min(b, d)

## Problems Covered

1. Introduction to Intervals
2. Merge Overlapping Intervals
3. Identify All Interval Overlaps
4. Largest Overlap of Intervals

## Interview Tips for Intervals

💡 **Key Interview Tips:**

1. **Sort strategically** - Most interval problems benefit from sorting by start time (sometimes end time)
2. **Define overlap precisely** - Clarify whether endpoints count as overlap [a,b] and [b,c]
3. **Visualize with timelines** - Draw intervals on paper to understand the problem better
4. **Handle edge cases systematically** - Empty lists, single intervals, no overlaps, identical times
5. **Consider greedy approaches** - Many interval problems have elegant greedy solutions
6. **Think about data structures** - Priority queues for meeting rooms, sweep line for complex problems
7. **Optimize for the use case** - Real-time insertions vs batch processing

### Comprehensive Interval Algorithms and Patterns

**1. Core Interval Operations:**

```python
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __repr__(self):
        return f"[{self.start}, {self.end}]"
    
    def overlaps(self, other):
        """Check if two intervals overlap"""
        return max(self.start, other.start) < min(self.end, other.end)
    
    def merge_with(self, other):
        """Merge with another overlapping interval"""
        return Interval(min(self.start, other.start), max(self.end, other.end))

def merge_intervals_comprehensive(intervals):
    """Merge overlapping intervals with detailed handling"""
    if not intervals:
        return []
    
    # Sort by start time, then by end time
    intervals.sort(key=lambda x: (x[0], x[1]))
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        last_merged = merged[-1]
        
        if current[0] <= last_merged[1]:  # Overlapping
            # Merge by extending the end time
            merged[-1] = [last_merged[0], max(last_merged[1], current[1])]
        else:  # Non-overlapping
            merged.append(current)
    
    return merged

def insert_interval_optimized(intervals, new_interval):
    """Insert interval and merge overlaps efficiently"""
    if not intervals:
        return [new_interval]
    
    result = []
    i = 0
    start, end = new_interval
    
    # Add all intervals that end before new interval starts
    while i < len(intervals) and intervals[i][1] < start:
        result.append(intervals[i])
        i += 1
    
    # Merge all overlapping intervals
    while i < len(intervals) and intervals[i][0] <= end:
        start = min(start, intervals[i][0])
        end = max(end, intervals[i][1])
        i += 1
    
    result.append([start, end])
    
    # Add all remaining intervals
    while i < len(intervals):
        result.append(intervals[i])
        i += 1
    
    return result
```

**2. Meeting Rooms and Scheduling Problems:**

```python
def can_attend_all_meetings(intervals):
    """Check if person can attend all meetings (no overlaps)"""
    if len(intervals) <= 1:
        return True
    
    intervals.sort(key=lambda x: x[0])
    
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False
    
    return True

def min_meeting_rooms(intervals):
    """Find minimum number of meeting rooms needed"""
    if not intervals:
        return 0
    
    # Separate start and end times
    start_times = sorted([interval[0] for interval in intervals])
    end_times = sorted([interval[1] for interval in intervals])
    
    start_ptr = end_ptr = 0
    rooms_used = max_rooms = 0
    
    while start_ptr < len(intervals):
        # A meeting starts
        if start_times[start_ptr] < end_times[end_ptr]:
            rooms_used += 1
            max_rooms = max(max_rooms, rooms_used)
            start_ptr += 1
        else:
            # A meeting ends
            rooms_used -= 1
            end_ptr += 1
    
    return max_rooms

def min_meeting_rooms_heap(intervals):
    """Alternative solution using min heap"""
    if not intervals:
        return 0
    
    import heapq
    intervals.sort(key=lambda x: x[0])
    
    # Min heap to track end times of ongoing meetings
    heap = []
    
    for start, end in intervals:
        # Remove meetings that have ended
        while heap and heap[0] <= start:
            heapq.heappop(heap)
        
        # Add current meeting's end time
        heapq.heappush(heap, end)
    
    return len(heap)

def meeting_rooms_schedule(intervals):
    """Return which room each meeting should be in"""
    if not intervals:
        return []
    
    import heapq
    
    # Sort meetings by start time, keep original indices
    indexed_intervals = [(intervals[i][0], intervals[i][1], i) for i in range(len(intervals))]
    indexed_intervals.sort()
    
    # Heap: (end_time, room_id)
    available_rooms = []
    room_assignments = [0] * len(intervals)
    next_room_id = 0
    
    for start, end, original_idx in indexed_intervals:
        # Free up rooms that have finished
        while available_rooms and available_rooms[0][0] <= start:
            heapq.heappop(available_rooms)
        
        if available_rooms:
            # Reuse an available room
            end_time, room_id = heapq.heappop(available_rooms)
            room_assignments[original_idx] = room_id
        else:
            # Need a new room
            room_assignments[original_idx] = next_room_id
            next_room_id += 1
        
        # Add room back to heap with new end time
        heapq.heappush(available_rooms, (end, room_assignments[original_idx]))
    
    return room_assignments
```

**3. Advanced Interval Problems:**

```python
def interval_intersection(list1, list2):
    """Find intersection of two interval lists"""
    result = []
    i = j = 0
    
    while i < len(list1) and j < len(list2):
        # Find the intersection
        start = max(list1[i][0], list2[j][0])
        end = min(list1[i][1], list2[j][1])
        
        # If there's an intersection
        if start < end:
            result.append([start, end])
        
        # Move the interval that ends first
        if list1[i][1] < list2[j][1]:
            i += 1
        else:
            j += 1
    
    return result

def remove_covered_intervals(intervals):
    """Remove intervals that are covered by other intervals"""
    intervals.sort(key=lambda x: (x[0], -x[1]))
    
    result = []
    for interval in intervals:
        # If result is empty or current interval is not covered
        if not result or interval[1] > result[-1][1]:
            result.append(interval)
    
    return result

def non_overlapping_intervals(intervals):
    """Find minimum number of intervals to remove to make non-overlapping"""
    if len(intervals) <= 1:
        return 0
    
    # Sort by end time (greedy choice)
    intervals.sort(key=lambda x: x[1])
    
    count = 0
    last_end = intervals[0][1]
    
    for i in range(1, len(intervals)):
        if intervals[i][0] < last_end:
            # Overlapping interval, need to remove
            count += 1
        else:
            # Update last end time
            last_end = intervals[i][1]
    
    return count

def max_events_attended(events):
    """Maximum number of events that can be attended"""
    events.sort(key=lambda x: x[1])  # Sort by end time
    
    count = 0
    last_end = 0
    
    for start, end in events:
        if start >= last_end:
            count += 1
            last_end = end
    
    return count
```

**4. Range and Sweep Line Algorithms:**

```python
class Event:
    def __init__(self, time, event_type, interval_id=None):
        self.time = time
        self.type = event_type  # 'start' or 'end'
        self.interval_id = interval_id
    
    def __lt__(self, other):
        if self.time != other.time:
            return self.time < other.time
        # End events come before start events at same time
        return self.type == 'end' and other.type == 'start'

def max_overlapping_intervals(intervals):
    """Find maximum number of overlapping intervals at any point"""
    events = []
    
    for i, (start, end) in enumerate(intervals):
        events.append(Event(start, 'start', i))
        events.append(Event(end, 'end', i))
    
    events.sort()
    
    current_overlap = 0
    max_overlap = 0
    
    for event in events:
        if event.type == 'start':
            current_overlap += 1
            max_overlap = max(max_overlap, current_overlap)
        else:
            current_overlap -= 1
    
    return max_overlap

def point_coverage(intervals, points):
    """Find which points are covered by intervals"""
    intervals.sort()
    points_with_index = [(points[i], i) for i in range(len(points))]
    points_with_index.sort()
    
    result = [False] * len(points)
    interval_idx = 0
    
    for point, original_idx in points_with_index:
        # Move to intervals that could contain this point
        while interval_idx < len(intervals) and intervals[interval_idx][1] < point:
            interval_idx += 1
        
        # Check if any interval contains this point
        for i in range(interval_idx, len(intervals)):
            if intervals[i][0] <= point <= intervals[i][1]:
                result[original_idx] = True
                break
            elif intervals[i][0] > point:
                break
    
    return result
```

**5. Optimization and Advanced Techniques:**

```python
class IntervalTree:
    """Efficient data structure for interval queries"""
    
    def __init__(self, intervals):
        self.intervals = intervals
        self.tree = self._build_tree(intervals)
    
    def _build_tree(self, intervals):
        if not intervals:
            return None
        
        # Find median point
        points = []
        for start, end in intervals:
            points.extend([start, end])
        points.sort()
        median = points[len(points) // 2]
        
        # Partition intervals
        left_intervals = []
        right_intervals = []
        center_intervals = []
        
        for interval in intervals:
            start, end = interval
            if end < median:
                left_intervals.append(interval)
            elif start > median:
                right_intervals.append(interval)
            else:
                center_intervals.append(interval)
        
        return {
            'median': median,
            'center': center_intervals,
            'left': self._build_tree(left_intervals),
            'right': self._build_tree(right_intervals)
        }
    
    def query_point(self, point):
        """Find all intervals containing the point"""
        return self._query_point(self.tree, point)
    
    def _query_point(self, node, point):
        if not node:
            return []
        
        result = []
        
        # Check center intervals
        for interval in node['center']:
            if interval[0] <= point <= interval[1]:
                result.append(interval)
        
        # Recurse to appropriate subtree
        if point < node['median']:
            result.extend(self._query_point(node['left'], point))
        else:
            result.extend(self._query_point(node['right'], point))
        
        return result

def merge_intervals_streaming(interval_stream):
    """Merge intervals as they arrive in a stream"""
    merged = []
    
    for new_interval in interval_stream:
        # Binary search for insertion point
        left, right = 0, len(merged)
        
        while left < right:
            mid = (left + right) // 2
            if merged[mid][0] < new_interval[0]:
                left = mid + 1
            else:
                right = mid
        
        # Insert and merge
        merged.insert(left, new_interval)
        
        # Merge with neighbors
        i = left
        while i > 0 and merged[i-1][1] >= merged[i][0]:
            # Merge with previous
            merged[i-1] = [merged[i-1][0], max(merged[i-1][1], merged[i][1])]
            merged.pop(i)
            i -= 1
        
        while i < len(merged) - 1 and merged[i][1] >= merged[i+1][0]:
            # Merge with next
            merged[i] = [merged[i][0], max(merged[i][1], merged[i+1][1])]
            merged.pop(i+1)
    
    return merged
```

### Problem-Solving Strategy and Pattern Recognition

**Step-by-Step Approach for Interval Problems:**

1. **Understand the problem type:**
   - Single interval list vs multiple lists
   - Need to merge, count, or find intersections
   - Real-time processing vs batch processing

2. **Choose the right sorting strategy:**
   - Sort by start time: Most merge problems
   - Sort by end time: Activity selection, greedy scheduling
   - Sort by both: Remove covered intervals

3. **Select appropriate algorithm:**
   - Simple iteration: Basic merging
   - Two pointers: Intersection of two lists
   - Heap/Priority queue: Meeting rooms, streaming
   - Sweep line: Complex overlap counting

**Decision Tree:**
```
Interval problem type?
├── Merge overlapping → Sort by start, iterate and merge
├── Scheduling/Meeting rooms → Sort by start, use heap for rooms
├── Intersection → Two pointers on sorted lists
├── Remove covered → Sort by start (desc by end), greedy selection
├── Count overlaps → Sweep line algorithm
└── Real-time updates → Interval tree or segment tree
```

### Advanced Problem Patterns

**Calendar and Scheduling Systems:**
```python
class MyCalendar:
    """Book meetings without double booking"""
    
    def __init__(self):
        self.calendar = []
    
    def book(self, start, end):
        for existing_start, existing_end in self.calendar:
            if start < existing_end and end > existing_start:
                return False
        
        self.calendar.append((start, end))
        return True

class MyCalendarTwo:
    """Allow at most double booking"""
    
    def __init__(self):
        self.calendar = []
        self.overlaps = []
    
    def book(self, start, end):
        # Check if it would create triple booking
        for overlap_start, overlap_end in self.overlaps:
            if start < overlap_end and end > overlap_start:
                return False
        
        # Add overlaps with existing bookings
        for cal_start, cal_end in self.calendar:
            if start < cal_end and end > cal_start:
                self.overlaps.append((max(start, cal_start), min(end, cal_end)))
        
        self.calendar.append((start, end))
        return True
```

**Resource Allocation and Optimization:**
```python
def min_platforms(arrivals, departures):
    """Minimum platforms needed at railway station"""
    arrivals.sort()
    departures.sort()
    
    platforms_needed = 0
    max_platforms = 0
    i = j = 0
    
    while i < len(arrivals) and j < len(departures):
        if arrivals[i] <= departures[j]:
            platforms_needed += 1
            max_platforms = max(max_platforms, platforms_needed)
            i += 1
        else:
            platforms_needed -= 1
            j += 1
    
    return max_platforms

def car_pooling(trips, capacity):
    """Check if car pooling is possible with given capacity"""
    events = []
    
    for num_passengers, start, end in trips:
        events.append((start, num_passengers))
        events.append((end, -num_passengers))
    
    events.sort()
    
    current_passengers = 0
    for location, passenger_change in events:
        current_passengers += passenger_change
        if current_passengers > capacity:
            return False
    
    return True
```

### Common Pitfalls and Expert Solutions

1. **Boundary Definition Issues**
   ```python
   # ❌ Wrong: Unclear overlap definition
   def overlaps_ambiguous(interval1, interval2):
       return interval1[1] >= interval2[0] and interval2[1] >= interval1[0]
   
   # ✅ Correct: Clear overlap definition
   def overlaps_clear(interval1, interval2):
       # Intervals [a,b] and [c,d] overlap if max(a,c) < min(b,d)
       return max(interval1[0], interval2[0]) < min(interval1[1], interval2[1])
   ```

2. **Sorting Strategy Errors**
   ```python
   # ❌ Wrong: Sorting only by start time for activity selection
   def wrong_activity_selection(activities):
       activities.sort(key=lambda x: x[0])  # Wrong sort criterion
       # ... rest of algorithm
   
   # ✅ Correct: Sort by end time for activity selection
   def correct_activity_selection(activities):
       activities.sort(key=lambda x: x[1])  # Correct sort criterion
       count = 0
       last_end = 0
       
       for start, end in activities:
           if start >= last_end:
               count += 1
               last_end = end
       
       return count
   ```

3. **Edge Case Handling**
   ```python
   def robust_merge_intervals(intervals):
       if not intervals:
           return []
       
       if len(intervals) == 1:
           return intervals
       
       # Handle invalid intervals
       valid_intervals = [(start, end) for start, end in intervals if start <= end]
       if not valid_intervals:
           return []
       
       # Sort and merge
       valid_intervals.sort()
       merged = [valid_intervals[0]]
       
       for start, end in valid_intervals[1:]:
           if start <= merged[-1][1]:
               merged[-1] = (merged[-1][0], max(merged[-1][1], end))
           else:
               merged.append((start, end))
       
       return merged
   ```

### Performance Analysis and Optimization

**Time Complexity Analysis:**

| Operation | Brute Force | Optimized | Data Structure |
|-----------|-------------|-----------|---------------|
| Merge intervals | O(n²) | O(n log n) | Sort + scan |
| Insert interval | O(n²) | O(n) | Binary search + merge |
| Meeting rooms | O(n²) | O(n log n) | Sort + heap |
| Interval intersection | O(n×m) | O(n + m) | Two pointers |
| Point queries | O(n) | O(log n) | Interval tree |

**Space Optimization Techniques:**
```python
def space_optimized_merge(intervals):
    """Merge intervals in-place when possible"""
    if len(intervals) <= 1:
        return intervals
    
    intervals.sort()
    write_index = 0
    
    for read_index in range(1, len(intervals)):
        current = intervals[read_index]
        last_merged = intervals[write_index]
        
        if current[0] <= last_merged[1]:
            # Merge in-place
            intervals[write_index][1] = max(last_merged[1], current[1])
        else:
            # Move to next position
            write_index += 1
            intervals[write_index] = current
    
    return intervals[:write_index + 1]
```

### Testing and Validation Framework

**Comprehensive Test Suite:**
```python
def test_interval_algorithms():
    """Test suite for interval algorithms"""
    
    test_cases = [
        # Basic cases
        ([], []),
        ([[1, 3]], [[1, 3]]),
        ([[1, 4], [4, 5]], [[1, 5]]),
        
        # Overlapping cases
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        ([[1, 4], [0, 4]], [[0, 4]]),
        ([[1, 4], [2, 3]], [[1, 4]]),
        
        # Edge cases
        ([[1, 4], [0, 0]], [[0, 0], [1, 4]]),
        ([[0, 1], [1, 2], [2, 3]], [[0, 3]]),
        ([[1, 1], [2, 2], [3, 3]], [[1, 1], [2, 2], [3, 3]]),
    ]
    
    for intervals, expected in test_cases:
        result = merge_intervals_comprehensive(intervals)
        status = "PASS" if result == expected else "FAIL"
        print(f"Input: {intervals} → Output: {result} ({status})")

def benchmark_interval_algorithms():
    """Performance benchmark for different approaches"""
    import time
    import random
    
    sizes = [100, 1000, 10000]
    
    for size in sizes:
        # Generate random intervals
        intervals = []
        for _ in range(size):
            start = random.randint(0, 1000)
            end = random.randint(start, start + 100)
            intervals.append([start, end])
        
        # Benchmark merge operations
        start_time = time.time()
        merge_intervals_comprehensive(intervals.copy())
        merge_time = time.time() - start_time
        
        start_time = time.time()
        space_optimized_merge(intervals.copy())
        optimized_time = time.time() - start_time
        
        print(f"Size {size}: Standard={merge_time:.4f}s, Optimized={optimized_time:.4f}s")
```

### Real-World Applications

**1. Calendar Applications:**
- Double booking prevention
- Meeting room scheduling
- Resource allocation
- Time slot availability

**2. System Design:**
- Rate limiting with time windows
- Log aggregation by time ranges
- Database query optimization
- Cache expiration management

**3. Financial Systems:**
- Trading session management
- Market hours handling
- Settlement period calculations
- Risk exposure time windows

**4. Transportation:**
- Route scheduling
- Vehicle allocation
- Traffic pattern analysis
- Delivery time windows

---
*Master interval algorithms to solve scheduling, calendar, and range-based problems efficiently!*