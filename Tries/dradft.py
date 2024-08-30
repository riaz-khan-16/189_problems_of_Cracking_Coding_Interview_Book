# Implement a Trie

class TrieNode:
    
    def __init__(self):
        self.children={}
        self.isEndofWord=False


class Trie:
     
    def __init__(self):
         self.root=TrieNode()
    def insert(self,word):
        current=self.root
        for i in word:
            if i not in current.children:
                current.children[i]=TrieNode()
            current=current.children[i]
        current.isEndofWord=True

         