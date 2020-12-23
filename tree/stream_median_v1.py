from binarytree import Node
from random import randrange
import math

def median(stream):
    sorted_stream = sorted(stream)
    if len(stream)%2 == 1:
        return( sorted_stream[len(stream)//2])
    else:
        a=sorted_stream[len(stream)//2-1]
        b=sorted_stream[len(stream)//2]
        return((a+b)/2)

class NodeTree(Node):

    def __init__(self,num=None):
        self.count = 1 if num is not None else 0
        self.val = num
        self.left = None
        self.right = None
        
class MedianOfAStream:

  def __init__(self):
      self.size = 0
      self.root = None

  def insert_num(self, num):
    self.size+=1
    if not self.root:
       self.root = NodeTree(num)
       return
    node = self.root
    while node:
        if node.val == num:
            node.count+=1
            print(num,node.count)
            return
        if node.val < num:
            if node.right:
                node = node.right
            else:
                node.right = NodeTree(num)
                return
        if node.val > num:
            if node.left:
                node = node.left
            else:
                node.left = NodeTree(num)
                return
    return

  def print_tree(self):
    print(self.root)

  def find_median(self):
    # TODO: Write your code here
    return 0.0
  
stream = MedianOfAStream()

array = []
for i in range(30):
    rn=randrange(100)
    array.append(rn)
    stream.insert_num(rn)
    stream.print_tree()
    print(array)
    print(sorted(array))
    print(median(array))
 