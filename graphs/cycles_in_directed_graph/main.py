import sys
sys.path.append('../')

from Graph import Graph
from Queue import MyQueue
from Stack import MyStack
# You can check the input directed graph in console tab

# Create Stack => stack = MyStack()
# Functions of Stack => push(int), pop(), top(), is_empty()
# Create Queue => queue = MyQueue()
# Functions of Queue => enqueue(int), dequeue(), size(), front(), is_empty()
# class Graph => {int vertices, linkedList[] array}
# class linkedList => {Node head_node}
# class Node => {int data, Node next_element}
# Depth First Traversal of Graph "g" from source vertex

def detect_cycle_helper(g,start,visited):
    node = g.array[start].get_head()
    while node:
        next_level_visited = visited + [node.data]
        if (node.data in visited) or detect_cycle_helper(g,node.data,next_level_visited):
            return True
        node = node.next_element
    return False

def detect_cycle(g): 
    for node in range(len(g.array)):
        if detect_cycle_helper(g,node,[node]):
            return True
    return False
  
g = Graph(7)

g.add_edge(0,3)
g.add_edge(0,4)
g.add_edge(0,5)

g.add_edge(1,0) 
g.add_edge(1,4)
g.add_edge(1,6)

#g.add_edge(2,1) # - remove loop

g.add_edge(4,2)

print(detect_cycle(g))
