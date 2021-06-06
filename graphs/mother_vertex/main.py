import sys
sys.path.append('../')

from Graph import Graph
from Queue import MyQueue
from Stack import MyStack
# You can check the input graph in console tab

# Create Stack => stack = MyStack()
# Functions of Stack => push(int), pop(), top(), is_empty()
# Create Queue => queue = MyQueue()
# Functions of Queue => enqueue(int), dequeue(), size(), front(), is_empty()
# class Graph => {int vertices, linkedList[] array}
# class linkedList => {Node head_node}
# class Node => {int data, Node next_element}


def find_mother_vertex(g):
    # Write - Your - Code
    for vertex in range(len(g.array)):
        if is_mother(vertex,g):
            return(vertex)
    return False

# Create helper functions here
def is_mother(vertex,g):
    print("Called with vertex=",vertex)
    visited = [False]*len(g.array)

    stack = MyStack()
    stack.push(vertex)

    while stack.size() > 0:
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            node = g.array[v].get_head()
            while node:
                stack.push(node.data)
                node = node.next_element
    return all(visited)