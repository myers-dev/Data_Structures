'''
Implementation of heap , based on list
Supported the following operations:
EXTRACT-MIN
DECREASE-KEY
INSERT
+HEAPIFY-UP (SHIFT-UP)
+HEAPIFY-DOWN (SHIFT-DOWN)
+DELETE

Numbering of the tree nodes are as follows:
    __0__
   /     \
  1       2
 / \     / \
3   4   5   6

Addressing in list [0,1,2,3,4,5,6,7]

Parent node , based on index in array : parent = (idx - 1)//2
Children nodes, based on index in array : childrens = ((idx+1)*2 - 1 , (idx+1)*2)

Implementation is usig zero-based indeces 

'''
from binarytree import Node
from binarytree import build
from random import randint

class Heap:
    def __init__(self,n=None):
        if n:
            self.heap = [n]
        else:
            self.heap = []
        self.length = len(self.heap)
        self.visualize = True

    def parent(self,idx):
        return (( idx - 1 )//2 )

    def children_left(self,idx):
        return ( idx*2 + 1 )

    def children_right(self,idx):
        return ( idx*2 + 2 )

    def heapify_up(self,idx):
        #self.show(f"heapifying up {idx}")
        while idx > 0 and self.heap[self.parent(idx)] > self.heap[idx]:
            #self.show(f"Performing swap between indexes {self.parent(idx)} and {idx} , values {self.heap[self.parent(idx)]} , {self.heap[idx]}")
            self.heap[self.parent(idx)],self.heap[idx] = self.heap[idx],self.heap[self.parent(idx)]
            #self.show(f"Resulting tree after swap")
            idx = self.parent(idx)
        #self.show(f"Heapify finished on {idx}")
        return
    
    def heapify_down(self,idx):
        '''
        Bubble down ; The key idea is to swap the root node with the smaller of its two children
        '''
        swap = True
        while swap:
            swap = False
            if self.children_left(idx) < len(self.heap) and \
               self.children_right(idx) < len(self.heap) :
                # both exists
                if self.heap[self.children_left(idx)] <= self.heap[self.children_right(idx)]:
                    if self.heap[self.children_left(idx)] < self.heap[idx]:
                        # Bubble down on left !
                        swap = True
                        self.heap[self.children_left(idx)],self.heap[idx] = \
                        self.heap[idx],self.heap[self.children_left(idx)]
                        idx = self.children_left(idx)
                elif self.heap[self.children_left(idx)] > self.heap[self.children_right(idx)]:
                    if self.heap[self.children_right(idx)] < self.heap[idx]:
                        # Bubble down on right !
                        swap = True
                        self.heap[self.children_right(idx)],self.heap[idx] = \
                        self.heap[idx],self.heap[self.children_right(idx)]
                        idx = self.children_right(idx)                    
            elif self.children_left(idx) < len(self.heap):
                # only left exist
                if self.heap[self.children_left(idx)] < self.heap[idx]:
                    # Bubble down on left !
                    swap = True
                    self.heap[self.children_left(idx)],self.heap[idx] = \
                    self.heap[idx],self.heap[self.children_left(idx)]
                    idx = self.children_left(idx)
            elif self.children_right(idx) < len(self.heap):
                # only right exist
                if self.heap[self.children_right(idx)] < self.heap[idx]:
                    # Bubble down on left !
                    swap = True
                    self.heap[self.children_right(idx)],self.heap[idx] = \
                    self.heap[idx],self.heap[self.children_right(idx)]
                    idx = self.children_right(idx) 
            #self.show("Was another swap...")              

        #self.show(f"Final : Extracted {result_min}")
        return
    
    def delete(self,idx):
        '''
        to be implemented
        '''
        return

    def show(self,message):
        '''
        Visualization of the heap as a binary tree
        '''
        if not self.visualize:
            return
        root = build(self.heap)
        if message:
            print(f">>> {message} <<<")
        print(root)

    def insert(self,n):
        # Inserting as a last element
        self.heap.append(n)
        self.heapify_up(len(self.heap) - 1)
        #self.show(f"Inserted {n}")

    def extract_min(self):
        result_min = self.heap[0] 
        #self.show(f'We are extracting {result_min}')
        if len(self.heap) == 1:
            self.heap.pop()
            return(result_min)
        '''
        Swapping last element and root
        '''
        self.heap[0]=self.heap.pop()
        #self.show(f'Swapping last element={self.heap[0]} and root={result_min}')
        '''
        Bubble down ; The key idea is to swap the root node with the smaller of its two children
        '''
        self.heapify_down(0)
        #self.show(f"Final : Extracted {result_min}")
        return(result_min)

def main():
    h = Heap()

    for i in range(100):
        h.insert(randint(0,100))
    s = []
    for i in range(100):
        s.append(h.extract_min())
    print(s)
    print(all([s[i] <= s[i+1] for i in range(len(s)-2)]))


main()