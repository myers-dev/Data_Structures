import sys
sys.path.append('./hash')

from HashTable import HashTable

def is_formation_possible(lst, word):
    h = HashTable()
    for wi in range(len(lst)):
        h.insert(lst[wi],wi)
    for i in range(len(word)):
        if h.search(word[0:i]) is not None and h.search(word[i:]) is not None:
            return (True)

    return (False)


lst = ["the", "hello", "there", "answer", "any",
       "by", "world", "their","abc"]

word = "helloworld"

print (is_formation_possible(lst,word))