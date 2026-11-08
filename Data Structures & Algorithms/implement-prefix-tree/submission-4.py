class TreeNode:
    def __init__(self, endOfWord = False):
        self.children = dict()
        self.endOfWord = endOfWord

class PrefixTree:

    def __init__(self):
        self.root = TreeNode(endOfWord = True)


    def insert(self, word: str) -> None:
        # Time complexity: O(len(word))

        # get the current root node
        node = self.root

        # iterate over each character in word
        for c in word:

            # if char not in trie, add char
            if c not in node.children.keys():
                node.children[c] = TreeNode()

            # iterate to next node
            node = node.children[c]

        node.endOfWord = True

        
    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node.children.keys():
                return False
            node = node.children[c]

        return node.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node.children.keys():
                return False
            node = node.children[c]

        return True
        
        