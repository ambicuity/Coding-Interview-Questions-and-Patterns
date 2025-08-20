# Tries Pattern

**Author:** Ritesh Rana

## Introduction to Tries

A Trie (pronounced "try"), also known as a prefix tree, is a tree-like data structure used to store and retrieve strings efficiently. Each node represents a character, and paths from root to nodes represent prefixes of stored strings. Tries are particularly useful for problems involving word searches, autocomplete functionality, and string prefix matching.

### Key Concepts

**Basic Structure:**
- **Root**: Empty node representing start of all strings
- **Nodes**: Each node contains character information and children
- **Paths**: Root-to-node paths represent string prefixes
- **End Markers**: Indicate complete word endings
- **Children**: Usually stored as array or hashmap

**Properties:**
- All descendants of a node share common prefix
- Root represents empty string
- Leaves often (but not always) represent complete words
- Time complexity proportional to string length, not number of strings

### Common Patterns

1. **Word Dictionary** - Storing and searching words
2. **Prefix Matching** - Finding all words with given prefix
3. **Autocomplete** - Suggesting word completions
4. **Wildcard Matching** - Searching with '.' wildcards
5. **Longest Common Prefix** - Finding common prefixes
6. **Word Search Games** - Finding words in character grids

### When to Use Tries

- Dictionary/vocabulary storage
- Autocomplete systems
- Spell checkers
- IP routing tables
- String prefix queries
- Word game implementations (Boggle, Scrabble)

### Time and Space Complexity

**Time Complexity:**
- Insert: O(m) where m is string length
- Search: O(m) where m is string length
- Prefix Search: O(p + n) where p is prefix length, n is number of results

**Space Complexity:** O(ALPHABET_SIZE * N * M) in worst case
where N is number of strings, M is average string length

## Problems Covered

1. Introduction to Tries
2. Design a Trie
3. Insert and Search Words with Wildcards
4. Find All Words on a Board

## Interview Tips for Tries

💡 **Key Interview Tips:**

1. **Consider alphabet size** - Affects space complexity and implementation
2. **Mark word endings** - Use boolean flag or special character
3. **Handle case sensitivity** - Normalize input if needed
4. **Think about memory** - Tries can be memory-intensive
5. **DFS for word finding** - Often combined with backtracking

### Implementation Examples

**Basic Trie Node:**
```python
class TrieNode:
    def __init__(self):
        self.children = {}  # or [None] * 26 for lowercase letters
        self.is_end_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_word = True
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_word
    
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
```

**Word Search with Wildcards:**
```python
def search_with_wildcards(self, word):
    def dfs(node, i):
        if i == len(word):
            return node.is_end_word
        
        char = word[i]
        if char == '.':
            # Wildcard: try all possible characters
            for child in node.children.values():
                if dfs(child, i + 1):
                    return True
            return False
        else:
            # Regular character
            if char in node.children:
                return dfs(node.children[char], i + 1)
            return False
    
    return dfs(self.root, 0)
```

**Find All Words with Prefix:**
```python
def find_words_with_prefix(self, prefix):
    # Find the prefix node
    node = self.root
    for char in prefix:
        if char not in node.children:
            return []
        node = node.children[char]
    
    # DFS to find all words starting with prefix
    words = []
    def dfs(node, current_word):
        if node.is_end_word:
            words.append(prefix + current_word)
        
        for char, child in node.children.items():
            dfs(child, current_word + char)
    
    dfs(node, "")
    return words
```

### Advanced Techniques

**Compressed Trie (Radix Tree):**
Merge nodes with single child to save space

**AC Automaton:**
Extension of trie for multiple pattern matching

**Memory Optimization:**
Use arrays instead of hashmaps for fixed alphabets

### Common Pitfalls and How to Avoid Them

1. **Case Sensitivity**
   - Decide whether to be case-sensitive or not
   - Normalize input consistently

2. **Memory Usage**
   - Tries can use significant memory
   - Consider alternative data structures for small datasets

3. **Empty String Handling**
   - Handle empty strings appropriately
   - Consider root node implications

4. **Character Set**
   - Be clear about supported characters
   - Handle Unicode if needed

---
*Master trie operations to efficiently solve string prefix and search problems!*