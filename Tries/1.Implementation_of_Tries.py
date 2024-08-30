# How to insert in a Tries


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.isEndOfWord = True
    def search(self, word):
        """
        Search for a word in the Trie
        """
        node = self.root
        for char in word:
            # If the character is not found, the word does not exist
            if char not in node.children:
                return False
            # Move to the next node
            node = node.children[char]
        # Return True if the current node marks the end of a word
        return node.isEndOfWord
    
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            # If the character is not found, no word starts with this prefix
            if char not in node.children:
                return False
            # Move to the next node
            node = node.children[char]
        return True

# Initialize the Trie
trie = Trie()

# Insert words into the Trie
trie.insert("apple")
trie.insert("app")

# Search for words in the Trie
print(trie.search("apple"))  # Output: True
print(trie.search("app"))    # Output: True
print(trie.search("appl"))   # Output: False

# Check if any word starts with the given prefix
print(trie.starts_with("app"))  # Output: True
print(trie.starts_with("apx"))  # Output: False



