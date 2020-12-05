from Trie import Trie
from TrieNode import TrieNode

# Create Trie => trie = Trie()
# TrieNode => {children, is_end_word, char,
# mark_as_leaf(), unmark_as_leaf()}
# get_root => trie.get_root()
# Insert a Word => trie.insert(key)
# Search a Word => trie.search(key) return true or false
# Delete a Word => trie.delete(key)

def find_words_helper(node,word,result=[]):
    if not node:
        return

    word+= node.char

    if node.is_end_word:
        result.append(word)
    
    for child in node.children:
        if child:
            find_words_helper(child,word,result)

def find_words(root):
    result = []
    find_words_helper(root,'',result)
    return(result)


if __name__ == '__main__':
    t = Trie()

    t.insert('yellow')
    t.insert('a')
    t.insert('alpha')
    t.insert('beta')
    t.insert('terminal')
    t.insert('godzilla')
    t.insert('cherry')

    t.print_trie()

    print(find_words(t.root))