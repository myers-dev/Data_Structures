'''
You have to implement the num_edges() function which takes an undirected graph 
and computes the total number of bidirectional edges. 
'''

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


def num_edges(g):
    # Iterate over all edges (as a vertices) from the vertice [ vertice X -> vertice Y]
    # Upon counting the edge we will remove vertice X from vertice Y

    num_edges = 0
    for vertice in range(g.vertices):
        print(f"Processing vertice {vertice}")
        neighbor = g.array[vertice].get_head()
        while neighbor:
            num_edges+=1
            # Processing neighbor removal [ g.array[neighbor.data] --> vertice ]
            g.array[neighbor.data].delete(vertice)
            # Printing graph 
            #print(f"We counted for {neighbor.data}. Resultign graph is :")
            #g.print_graph()
            neighbor = neighbor.next_element
    return (num_edges)


g = Graph(9)
num_of_vertices = g.vertices
if(num_of_vertices == 0):
    print("Graph is empty")
elif(num_of_vertices < 0):
    print("Graph cannot have negative vertices")
else:
    g.add_edge(0, 2)
    g.add_edge(0, 5)

    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(2, 4)   

    g.add_edge(3, 2) 
    g.add_edge(3, 5)
    g.add_edge(3, 6)

    g.add_edge(4, 2)
    g.add_edge(4, 6)

    g.add_edge(5, 0)
    g.add_edge(5, 3)
    g.add_edge(5, 6)

    g.add_edge(6, 3)
    g.add_edge(6, 4)
    g.add_edge(6, 5)
    g.add_edge(6, 7)
    g.add_edge(6, 8)

    g.add_edge(7, 6)
    g.add_edge(7, 8)

    g.add_edge(8, 6)
    g.add_edge(8, 7)

    g.print_graph()

    print(num_edges(g))