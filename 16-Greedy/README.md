# Greedy Pattern

**Author:** Ritesh Rana

## Introduction to Greedy Algorithms

Greedy algorithms make locally optimal choices at each step with the hope of finding a global optimum. They are characterized by making the best choice available at the moment without considering the overall problem. While not always optimal, greedy algorithms are efficient and work well for many optimization problems with specific properties.

### Key Concepts

**Core Principles:**
- **Local Optimization**: Make the best choice at each step
- **No Backtracking**: Never reconsider previous choices
- **Irrevocable Decisions**: Once a choice is made, it's final
- **Efficiency**: Usually linear or O(n log n) time complexity

**Greedy Choice Property:**
A global optimum can be reached by making locally optimal choices.

**Optimal Substructure:**
Optimal solution contains optimal solutions to subproblems.

### Common Patterns

1. **Activity Selection** - Scheduling non-overlapping activities
2. **Fractional Knapsack** - Maximizing value with weight constraint
3. **Huffman Coding** - Optimal prefix-free codes
4. **Minimum Spanning Tree** - Connecting all nodes with minimum cost
5. **Shortest Path** - Dijkstra's algorithm for single-source shortest paths
6. **Job Scheduling** - Minimizing completion time or maximizing profit

### When to Use Greedy Algorithms

- Optimization problems where local optimal leads to global optimal
- When you can prove the greedy choice property
- Problems involving scheduling and resource allocation
- When dynamic programming would be overkill
- Time-sensitive applications requiring fast solutions

### Greedy vs Other Approaches

| Approach | Time Complexity | Optimality | Use Case |
|----------|----------------|------------|-----------|
| Greedy | Usually O(n log n) | Sometimes | Fast approximate solutions |
| Dynamic Programming | O(n²) or higher | Always | Complex optimization |
| Brute Force | Exponential | Always | Small inputs only |

## Problems Covered

1. Introduction to Greedy Algorithms
2. Jump to the End
3. Gas Stations
4. Candies

## Interview Tips for Greedy Algorithms

💡 **Key Interview Tips:**

1. **Prove greedy choice property** - Show local optimal leads to global optimal
2. **Consider counterexamples** - Verify greedy approach works for edge cases
3. **Sort when beneficial** - Many greedy problems benefit from sorting
4. **Think simple first** - Greedy solutions are often surprisingly simple
5. **Compare with DP** - Sometimes greedy is sufficient instead of complex DP

### Implementation Examples

**Activity Selection (Interval Scheduling):**
```python
def max_activities(start_times, end_times):
    n = len(start_times)
    activities = list(zip(start_times, end_times, range(n)))
    
    # Sort by end time (greedy choice)
    activities.sort(key=lambda x: x[1])
    
    selected = [activities[0][2]]  # Select first activity
    last_end_time = activities[0][1]
    
    for i in range(1, n):
        start_time, end_time, index = activities[i]
        
        # If this activity starts after the last selected ends
        if start_time >= last_end_time:
            selected.append(index)
            last_end_time = end_time
    
    return selected
```

**Fractional Knapsack:**
```python
def fractional_knapsack(weights, values, capacity):
    n = len(weights)
    
    # Calculate value-to-weight ratio for each item
    items = [(values[i] / weights[i], weights[i], values[i]) 
             for i in range(n)]
    
    # Sort by value-to-weight ratio in descending order
    items.sort(reverse=True)
    
    total_value = 0
    current_weight = 0
    
    for ratio, weight, value in items:
        if current_weight + weight <= capacity:
            # Take the whole item
            current_weight += weight
            total_value += value
        else:
            # Take fraction of the item
            remaining_capacity = capacity - current_weight
            total_value += ratio * remaining_capacity
            break
    
    return total_value
```

**Jump Game (Minimum Jumps):**
```python
def min_jumps(nums):
    if len(nums) <= 1:
        return 0
    
    jumps = 0
    current_end = 0
    farthest = 0
    
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        
        if i == current_end:
            jumps += 1
            current_end = farthest
            
            if current_end >= len(nums) - 1:
                break
    
    return jumps
```

**Gas Station Circuit:**
```python
def can_complete_circuit(gas, cost):
    total_tank = 0
    current_tank = 0
    starting_station = 0
    
    for i in range(len(gas)):
        total_tank += gas[i] - cost[i]
        current_tank += gas[i] - cost[i]
        
        # If we can't reach the next station
        if current_tank < 0:
            starting_station = i + 1
            current_tank = 0
    
    return starting_station if total_tank >= 0 else -1
```

**Meeting Rooms II (Minimum Rooms Needed):**
```python
def min_meeting_rooms(intervals):
    if not intervals:
        return 0
    
    # Separate start and end times
    start_times = sorted([interval[0] for interval in intervals])
    end_times = sorted([interval[1] for interval in intervals])
    
    start_pointer = end_pointer = 0
    rooms_needed = 0
    max_rooms = 0
    
    while start_pointer < len(intervals):
        # A meeting starts
        if start_times[start_pointer] < end_times[end_pointer]:
            rooms_needed += 1
            start_pointer += 1
        else:
            # A meeting ends
            rooms_needed -= 1
            end_pointer += 1
        
        max_rooms = max(max_rooms, rooms_needed)
    
    return max_rooms
```

### Proving Greedy Correctness

**Steps to Prove Greedy Algorithm:**
1. **Greedy Choice Property**: Show local optimal choice leads to global optimal
2. **Optimal Substructure**: Optimal solution contains optimal substructure
3. **Cut and Paste**: If greedy choice isn't optimal, you can modify optimal to include greedy choice

**Exchange Argument:**
Show that any optimal solution can be transformed into greedy solution without loss of optimality.

### Common Pitfalls and How to Avoid Them

1. **Assuming Greedy Always Works**
   - Not all optimization problems have greedy solutions
   - Always verify with examples and proof

2. **Wrong Greedy Choice**
   - Choosing wrong local optimization criterion
   - Consider different sorting orders or selection criteria

3. **Not Handling Edge Cases**
   - Empty inputs, single elements, impossible cases
   - Test with boundary conditions

4. **Ignoring Problem Constraints**
   - Ensure greedy choice respects all constraints
   - Consider feasibility along with optimality

---
*Master greedy algorithms to solve optimization problems efficiently with simple, elegant solutions!*