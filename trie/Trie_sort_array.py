from Trie import Trie
from TrieNode import TrieNode
from collections import deque

def sort_list(arr):
    t = Trie()
    for word in arr:
        t.insert(word)
    #t.print_trie()
    queue = deque()
    result = []

    for letter in t.get_root().children:
        if letter:
            queue.appendleft([letter,""])

    while queue:
        [node,word] = queue.pop()
        word+=node.char

        if node.is_end_word:
            result.append(word)

        for lidx in range(len(node.children)-1,-1,-1):
            letter = node.children[lidx]
            if letter:
                queue.append([letter,word])
        
    return(result)

if __name__ == '__main__':
    keys = ["the", "a", "there", "answer", "any",
                     "by", "bye", "their","abc"]
    print(sort_list(keys))