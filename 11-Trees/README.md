# Trees Pattern

**Author:** Ritesh Rana

## Introduction to Trees

Trees are hierarchical data structures consisting of nodes connected by edges. Each tree has a root node and zero or more subtrees. Binary trees, where each node has at most two children, are the most common type used in coding interviews. Tree problems often involve traversal, searching, manipulation, and structural analysis.

### Key Concepts

**Basic Terminology:**
- **Root**: The topmost node with no parent
- **Leaf**: A node with no children
- **Height**: Length of the longest path from root to leaf
- **Depth**: Distance from root to a specific node
- **Subtree**: A tree formed by a node and all its descendants

**Binary Tree Properties:**
- Each node has at most two children (left and right)
- Binary Search Tree (BST): Left < Root < Right for each subtree
- Complete Tree: All levels filled except possibly the last
- Perfect Tree: All internal nodes have two children, all leaves at same level

### Common Patterns

1. **Tree Traversal** - DFS (Inorder, Preorder, Postorder) and BFS
2. **Tree Construction** - Building trees from traversals
3. **Tree Validation** - Checking BST properties, balance, etc.
4. **Path Problems** - Finding paths with specific properties
5. **Tree Modification** - Inverting, flattening, pruning
6. **Level Processing** - Working with tree levels
7. **Ancestor Problems** - Finding LCA, path to root

### When to Use Trees

- Hierarchical data representation
- Fast searching in sorted data (BST)
- Expression parsing and evaluation
- File system representation
- Decision making processes
- Hierarchical clustering

### Tree Traversal Methods

**Depth-First Search (DFS):**
- **Inorder**: Left → Root → Right
- **Preorder**: Root → Left → Right  
- **Postorder**: Left → Right → Root

**Breadth-First Search (BFS):**
- **Level Order**: Process nodes level by level

## Problems Covered

1. Introduction to Trees
2. Invert Binary Tree
3. Balanced Binary Tree Validation
4. Rightmost Nodes of a Binary Tree
5. Widest Binary Tree Level
6. Binary Search Tree Validation
7. Lowest Common Ancestor
8. Build Binary Tree From Preorder and Inorder Traversals
9. Maximum Sum of a Continuous Path in a Binary Tree
10. Binary Tree Symmetry
11. Binary Tree Columns
12. Kth Smallest Number in a Binary Search Tree
13. Serialize and Deserialize a Binary Tree

## Interview Tips for Trees

💡 **Key Interview Tips:**

1. **Choose the right traversal** - DFS vs BFS based on problem requirements
2. **Master recursion** - Natural for tree problems but watch for stack overflow
3. **Handle null nodes** - Always check for null before accessing node properties
4. **Draw the tree** - Visualize on paper/whiteboard to understand better
5. **Consider edge cases** - Empty tree, single node, skewed trees, balanced trees
6. **Understand tree properties** - Height, depth, balance, completeness
7. **Use appropriate data structures** - Queues for BFS, stacks for iterative DFS

### Essential Tree Patterns and Implementations

**1. All Traversal Methods:**

```python
# Recursive DFS Traversals
def inorder_recursive(root):
    result = []
    def helper(node):
        if node:
            helper(node.left)
            result.append(node.val)
            helper(node.right)
    helper(root)
    return result

def preorder_recursive(root):
    result = []
    def helper(node):
        if node:
            result.append(node.val)
            helper(node.left)
            helper(node.right)
    helper(root)
    return result

def postorder_recursive(root):
    result = []
    def helper(node):
        if node:
            helper(node.left)
            helper(node.right)
            result.append(node.val)
    helper(root)
    return result

# Iterative DFS Traversals
def inorder_iterative(root):
    result, stack = [], []
    current = root
    
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        
        current = stack.pop()
        result.append(current.val)
        current = current.right
    
    return result

def preorder_iterative(root):
    if not root:
        return []
    
    result, stack = [], [root]
    
    while stack:
        node = stack.pop()
        result.append(node.val)
        
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return result

# BFS Level Order
def level_order_traversal(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result
```

**2. Tree Properties and Measurements:**

```python
def tree_height(root):
    if not root:
        return 0
    return 1 + max(tree_height(root.left), tree_height(root.right))

def tree_depth(root, target_node):
    if not root:
        return -1
    if root == target_node:
        return 0
    
    left_depth = tree_depth(root.left, target_node)
    if left_depth != -1:
        return left_depth + 1
    
    right_depth = tree_depth(root.right, target_node)
    if right_depth != -1:
        return right_depth + 1
    
    return -1

def is_balanced(root):
    def check_height(node):
        if not node:
            return 0
        
        left_height = check_height(node.left)
        if left_height == -1:
            return -1
        
        right_height = check_height(node.right)
        if right_height == -1:
            return -1
        
        if abs(left_height - right_height) > 1:
            return -1
        
        return 1 + max(left_height, right_height)
    
    return check_height(root) != -1

def count_nodes(root):
    if not root:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)
```

**3. Binary Search Tree Operations:**

```python
def insert_into_bst(root, val):
    if not root:
        return TreeNode(val)
    
    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    
    return root

def search_bst(root, val):
    if not root or root.val == val:
        return root
    
    if val < root.val:
        return search_bst(root.left, val)
    return search_bst(root.right, val)

def delete_from_bst(root, key):
    if not root:
        return root
    
    if key < root.val:
        root.left = delete_from_bst(root.left, key)
    elif key > root.val:
        root.right = delete_from_bst(root.right, key)
    else:
        # Node to delete found
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        
        # Node has two children: find inorder successor
        min_node = find_min(root.right)
        root.val = min_node.val
        root.right = delete_from_bst(root.right, min_node.val)
    
    return root

def find_min(node):
    while node.left:
        node = node.left
    return node
```

**4. Advanced Tree Problems:**

```python
# Lowest Common Ancestor
def lowest_common_ancestor(root, p, q):
    if not root or root == p or root == q:
        return root
    
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    
    if left and right:
        return root
    return left or right

# Maximum Path Sum
def max_path_sum(root):
    max_sum = float('-inf')
    
    def max_gain(node):
        nonlocal max_sum
        if not node:
            return 0
        
        left_gain = max(max_gain(node.left), 0)
        right_gain = max(max_gain(node.right), 0)
        
        price_newpath = node.val + left_gain + right_gain
        max_sum = max(max_sum, price_newpath)
        
        return node.val + max(left_gain, right_gain)
    
    max_gain(root)
    return max_sum

# Serialize and Deserialize
def serialize(root):
    def preorder(node):
        if not node:
            vals.append("#")
        else:
            vals.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
    
    vals = []
    preorder(root)
    return ','.join(vals)

def deserialize(data):
    def build_tree():
        val = next(vals)
        if val == "#":
            return None
        
        node = TreeNode(int(val))
        node.left = build_tree()
        node.right = build_tree()
        return node
    
    vals = iter(data.split(','))
    return build_tree()
```

**5. Tree Construction:**

```python
def build_tree_from_preorder_inorder(preorder, inorder):
    if not preorder or not inorder:
        return None
    
    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])
    
    root.left = build_tree_from_preorder_inorder(
        preorder[1:mid+1], inorder[:mid]
    )
    root.right = build_tree_from_preorder_inorder(
        preorder[mid+1:], inorder[mid+1:]
    )
    
    return root

def build_tree_from_postorder_inorder(postorder, inorder):
    if not postorder or not inorder:
        return None
    
    root = TreeNode(postorder[-1])
    mid = inorder.index(postorder[-1])
    
    root.left = build_tree_from_postorder_inorder(
        postorder[:mid], inorder[:mid]
    )
    root.right = build_tree_from_postorder_inorder(
        postorder[mid:-1], inorder[mid+1:]
    )
    
    return root
```

### Implementation Examples

**Basic Tree Node:**
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

**Inorder Traversal (Recursive):**
```python
def inorder_traversal(root):
    result = []
    
    def inorder(node):
        if node:
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
    
    inorder(root)
    return result
```

**Level Order Traversal (BFS):**
```python
from collections import deque

def level_order(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result
```

**Binary Search Tree Validation:**
```python
def is_valid_bst(root):
    def validate(node, min_val, max_val):
        if not node:
            return True
        
        if node.val <= min_val or node.val >= max_val:
            return False
        
        return (validate(node.left, min_val, node.val) and
                validate(node.right, node.val, max_val))
    
    return validate(root, float('-inf'), float('inf'))
```

### Advanced Tree Algorithms and Optimizations

**Threaded Binary Trees:**
```python
class ThreadedTreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
        self.left_thread = False
        self.right_thread = False

def create_threaded_tree(root):
    # Implementation for threading a binary tree
    # Allows O(1) successor/predecessor operations
    pass
```

**AVL Tree (Self-Balancing BST):**
```python
class AVLNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

def get_height(node):
    return node.height if node else 0

def get_balance(node):
    return get_height(node.left) - get_height(node.right) if node else 0

def rotate_right(y):
    x = y.left
    T2 = x.right
    
    x.right = y
    y.left = T2
    
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))
    
    return x

def rotate_left(x):
    y = x.right
    T2 = y.left
    
    y.left = x
    x.right = T2
    
    x.height = 1 + max(get_height(x.left), get_height(x.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    
    return y
```

**Segment Tree (Range Queries):**
```python
class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)
    
    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self.build(arr, 2 * node + 1, start, mid)
            self.build(arr, 2 * node + 2, mid + 1, end)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]
    
    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        
        mid = (start + end) // 2
        p1 = self.query(2 * node + 1, start, mid, l, r)
        p2 = self.query(2 * node + 2, mid + 1, end, l, r)
        return p1 + p2
```

### Tree Problem Solving Strategies

**When to Use Each Approach:**

| Problem Type | Best Approach | Time Complexity |
|--------------|---------------|----------------|
| Tree traversal | DFS (recursive) | O(n) |
| Level processing | BFS (iterative) | O(n) |
| Path finding | DFS with backtracking | O(n) |
| Range queries | Segment tree | O(log n) |
| Dynamic updates | Balanced BST (AVL/Red-Black) | O(log n) |
| Ancestor queries | DFS with parent tracking | O(n) preprocessing, O(1) query |

**Space Optimization Techniques:**
1. **Morris Traversal**: O(1) space inorder traversal
2. **Iterative approaches**: Reduce function call stack overhead
3. **In-place algorithms**: Modify tree structure temporarily

### Common Pitfalls and Solutions

1. **Stack Overflow with Deep Trees**
   - Use iterative approaches for very deep trees
   - Consider tail recursion optimization
   - Set appropriate recursion limits

2. **Memory Leaks**
   - Properly handle node deletion in manual memory management
   - Break circular references before deletion

3. **Integer Overflow in Calculations**
   - Use appropriate data types for tree values
   - Handle edge cases in mathematical operations

4. **Incorrect Tree Modification**
   - Always maintain tree invariants (BST property, balance, etc.)
   - Test tree structure after modifications

### Testing and Debugging Trees

**Tree Visualization:**
```python
def print_tree(root, level=0, prefix="Root: "):
    if root:
        print(" " * (level * 4) + prefix + str(root.val))
        if root.left or root.right:
            if root.left:
                print_tree(root.left, level + 1, "L--- ")
            else:
                print(" " * ((level + 1) * 4) + "L--- None")
            
            if root.right:
                print_tree(root.right, level + 1, "R--- ")
            else:
                print(" " * ((level + 1) * 4) + "R--- None")
```

**Tree Validation:**
```python
def validate_tree_structure(root):
    """Validate basic tree structure properties"""
    if not root:
        return True, "Empty tree is valid"
    
    # Check for cycles (simplified - use visited set for complete check)
    def has_cycle(node, visited):
        if not node:
            return False
        if node in visited:
            return True
        visited.add(node)
        return has_cycle(node.left, visited) or has_cycle(node.right, visited)
    
    if has_cycle(root, set()):
        return False, "Tree contains cycle"
    
    return True, "Tree structure is valid"

def validate_bst_property(root, min_val=float('-inf'), max_val=float('inf')):
    """Validate BST property"""
    if not root:
        return True
    
    if root.val <= min_val or root.val >= max_val:
        return False
    
    return (validate_bst_property(root.left, min_val, root.val) and
            validate_bst_property(root.right, root.val, max_val))
```
```python
def max_depth(root):
    if not root:
        return 0
    
    return 1 + max(max_depth(root.left), max_depth(root.right))
```

### Advanced Techniques

**Morris Traversal (O(1) Space):**
Inorder traversal without recursion or stack

**Serialization:**
Converting tree to string and back for storage/transmission

**Path Sum Problems:**
Finding paths with specific sum using backtracking

### Common Pitfalls and How to Avoid Them

1. **Null Pointer Exceptions**
   - Always check if node exists before accessing
   - Handle empty tree cases

2. **Stack Overflow**
   - For very deep trees, consider iterative approaches
   - Use explicit stack instead of recursion when needed

3. **Incorrect Base Cases**
   - Define proper termination conditions for recursion
   - Test with simple cases first

---
*Master tree algorithms to solve hierarchical data structure problems efficiently!*