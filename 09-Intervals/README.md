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

1. **Sort first** - Most interval problems become easier after sorting
2. **Define overlap clearly** - Understand whether endpoints count as overlap
3. **Handle edge cases** - Empty intervals, single intervals, no overlaps
4. **Draw diagrams** - Visualize intervals on a timeline
5. **Consider greedy approaches** - Many interval problems have greedy solutions

### Implementation Examples

**Merge Overlapping Intervals:**
```python
def merge_intervals(intervals):
    if not intervals:
        return []
    
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            # Overlapping intervals, merge them
            merged[-1][1] = max(merged[-1][1], end)
        else:
            # Non-overlapping interval
            merged.append([start, end])
    
    return merged
```

**Insert Interval:**
```python
def insert_interval(intervals, new_interval):
    result = []
    i = 0
    
    # Add intervals that end before new interval starts
    while i < len(intervals) and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1
    
    # Merge overlapping intervals with new interval
    while i < len(intervals) and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1
    
    result.append(new_interval)
    
    # Add remaining intervals
    result.extend(intervals[i:])
    
    return result
```

**Meeting Rooms Problem:**
```python
def can_attend_all_meetings(intervals):
    intervals.sort(key=lambda x: x[0])
    
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False
    
    return True
```

### Common Pitfalls and How to Avoid Them

1. **Sorting Strategy**
   - Choose appropriate sorting criterion (start vs end time)
   - Consider stability of sort when needed

2. **Boundary Conditions**
   - Handle inclusive vs exclusive endpoints correctly
   - Check edge cases with identical start/end times

3. **Memory Management**
   - Be efficient when merging intervals
   - Consider in-place modifications vs creating new arrays

---
*Master interval algorithms to solve scheduling and range-based problems efficiently!*