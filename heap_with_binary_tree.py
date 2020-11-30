'''
Implementation of heap , based on list
Supported the following operations:
EXTRACT-MIN
DECREASE-KEY
INSERT
+HEAPIFY-UP (SHIFT-UP)
+HEAPIFY-DOWN (SHIFT-DOWN)
+DELETE
++HEAPIFY

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
    def __init__(self,n=None,log=False):
        if n:
            self.heap = [n]
        else:
            self.heap = []
        self.visualize = True
        self.log = log

    def parent(self,idx):
        return (( idx - 1 )//2 )

    def children_left(self,idx):
        return ( idx*2 + 1 )

    def children_right(self,idx):
        return ( idx*2 + 2 )

    def length(self):
        return ( len(self.heap) )

    def heapify_up(self,idx):
        if self.log:
            self.show(f"heapifying up {idx}")
            pass
        while idx > 0 and self.heap[self.parent(idx)] > self.heap[idx]:
            if self.log:
                self.show(f"Performing swap between indexes {self.parent(idx)} and {idx} , values {self.heap[self.parent(idx)]} , {self.heap[idx]}")
                pass
            self.heap[self.parent(idx)],self.heap[idx] = self.heap[idx],self.heap[self.parent(idx)]
            if self.log:
                self.show(f"Resulting tree after swap")
                pass
            idx = self.parent(idx)
        if self.log:
            self.show(f"Heapify finished on {idx}")
            pass
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
            if self.log:
                self.show("Was another swap...") 
                pass             

        if self.log:
            self.show(f"Final : Heapify_down completed at {idx}")
            pass
        return
    
    def delete(self,idx):
        '''
        replacing target element with the last element,shrinking the heap and performing heapify down
        '''
        if self.log:
            self.show(f"Before deleting at index {idx}")
            pass
        #print(f"{self.heap} {idx}")
        if idx == len(self.heap) - 1:
            self.heap.pop()
            return

        self.heap[idx] = self.heap.pop()
        self.heapify_down(idx)
        if self.log:
            self.show(f"Delete at index {idx} performed")
            pass
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
        if self.log:
            self.show(f"Inserted {n}")
            pass

    def extract_min(self):
        if not self.heap:
            return(None)

        result_min = self.heap[0] 
        if self.log:
            self.show(f'We are extracting {result_min}')
            pass
        if len(self.heap) == 1:
            self.heap.pop()
            return(result_min)
        '''
        Swapping last element and root
        '''
        self.heap[0]=self.heap.pop()
        if self.log:
            self.show(f'Swapping last element={self.heap[0]} and root={result_min}')
            pass
        '''
        Bubble down ; The key idea is to swap the root node with the smaller of its two children
        '''
        self.heapify_down(0)
        if self.log:
            self.show(f"Final : Extracted {result_min}")
            pass
        return(result_min)

def heapify(self,lst):
    '''
    to be implemented
    '''
    return

def main():
    h = Heap()

    for i in range(100):
        h.insert(randint(0,100))
    # for i in range(16):
    #     h.delete(randint(0,h.length() - 1))
    s = []
    for i in range(100):
        s.append(h.extract_min())
    print(s)
    print(all([s[i] <= s[i+1] for i in range(len(s)-2)]))


main()