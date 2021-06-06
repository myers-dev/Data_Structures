'''

Implementation of Trie Node


'''



class TrieNode:
    def __init__(self,char = ''):
        self.children = [None] * 26   # Total size of English alphabed
        self.is_end_word = False     # True if thats an end of the word
        self.char = char.lower()

    def mark_as_leaf(self):
        self.is_end_word = True

    def unmark_as_leaf(self):
        self.is_end_word = False