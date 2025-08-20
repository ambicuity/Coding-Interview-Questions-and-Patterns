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

1. **Choose traversal method** - DFS vs BFS based on problem requirements
2. **Use recursion wisely** - Natural for tree problems but watch stack overflow
3. **Handle null nodes** - Always check for null before accessing
4. **Draw the tree** - Visualize to understand the problem better
5. **Consider edge cases** - Empty tree, single node, skewed tree

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

**Tree Height:**
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