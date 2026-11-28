class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.endOfWord = True
        

    def search(self, word: str) -> bool:

        def dfs(index, cur_node):
            if index == len(word): # base case: end of word
                return cur_node.endOfWord
            char = word[index]
            if char.isalpha() and char not in cur_node.children: # normal letter
                return False
            if char == ".": # wildcard .
                for child_node in cur_node.children.values(): 
                    if dfs(index + 1, child_node):
                        return True
                return False
            cur_node = cur_node.children[char]
            return dfs(index + 1, cur_node)

        return dfs(0, self.root)
        

    def normal_search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return cur.endOfWord
        
