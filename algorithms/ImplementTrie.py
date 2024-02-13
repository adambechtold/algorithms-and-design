"""
Implement Trie

link: https://leetcode.com/problems/implement-trie-prefix-tree/
author: adambechtold
date: 2024.02.13
difficulty: medium

- Runtime: beats 75%
- Memory: beats 49%

Big O Analysis
n = number of strings
m = length of largest string inserted
k = length of prefix

insert:     O(k)
search:     O(k)
startsWith: O(m)
"""

class CharNode:

    def __init__(self, char: str, is_word_end: bool=False):
        if len(char) > 1:
            raise ValueError("A CharNode can only hold a single character")
        
        self.value = char
        self.is_word_end = is_word_end
        self.next_nodes = dict()

class Trie:

    def __init__(self):
        self.root = CharNode('')

    def insert(self, word: str) -> None:
        current_node = self.root

        for char in word:
            if char in current_node.next_nodes:
                # Advance the current node to that char node
                current_node = current_node.next_nodes[char]
            else:
                # Add node and advance the current node to it
                new_node = CharNode(char)
                current_node.next_nodes[char] = new_node
                current_node = new_node
        
        # The current node is the final node
        current_node.is_word_end = True
        

    def search(self, word: str) -> bool:
        current_node = self.root

        for char in word:
            if char in current_node.next_nodes:
                current_node = current_node.next_nodes[char]
            else:
                return False

        return current_node.is_word_end

    def startsWith(self, prefix: str) -> bool:
        current_node = self.root

        for char in prefix:
            if char in current_node.next_nodes:
                current_node = current_node.next_nodes[char]
            else:
                return False
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)