from TrieNode import TrieNode

class Trie:
    def __init__(self):
        self.root = TrieNode() # Root Node

    def position(self,symbol):
        return(ord(symbol.lower()) - ord('a'))

    # Function to insert a key into the trie
    def insert(self, key):    
        if key is None:
            return

        key = key.lower()

        node = self.root

        for symbol in key:
            #print(f"Getting {symbol}")
            # Iterating over childrens 
            if node.children[self.position(symbol)] is None:
                #print(f"Creating {symbol}")
                node.children[self.position(symbol)] = TrieNode(symbol)
            #print(node.children)
            node = node.children[self.position(symbol)]
        node.is_end_word = True
    
        return()

    # Helper Function to return true if current_node does not have any children
    def has_no_children(self, current_node):   
        return(-1)

    # Recursive function to delete given key
    def delete_helper(self, key, current_node, length, level):
        return(-1)

    # Function to delete given key from Trie
    def delete(self, key):
        return(-1)

    def print_trie(self,node = None, word = ''):

        # Initiate print_trie for every node. Stop and print if is_end_word is set
        if node is None:
            node = self.root

        if node.char is not None:
            word+=node.char

        if node.is_end_word:
            print(word)

        #print('print_trie started')
        #print(node.children)

        for child in node.children:
            if child and child.char is not None:
                #print(f'->{child.char}')
                self.print_trie(child, word)

        return()

if __name__ == '__main__':

    t = Trie()

    t.insert('analgin')
    t.insert('analytic')
    t.insert('analysis')
    t.insert('computer')
    
    t.print_trie()