'''
Implement the total_words() function which will find the total number of words in a trie.
'''
from Trie import Trie
from TrieNode import TrieNode


# TrieNode => {children, is_end_word, char,
# mark_as_leaf(), unmark_as_leaf()}
def total_words(root):
    
    num = 1 if root.is_end_word else 0

    for child in root.children:
        if child:
            num+= total_words(child)
    
    return(num)