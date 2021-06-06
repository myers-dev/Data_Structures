'''
Implement the find_min() function which will take a directed graph and two vertices, A and B. The result will be the shortest path from A to B.

Remember, the shortest path will contain the minimum number of edges.

Input #
A directed graph, a vertex A and a vertex B.

Output #
Returns number of edges in the shortest path between A and B.
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

def find_min(g, source, destination):
    # Write your code here
    # find_min will be equal to find_min from all neighbors
    # 
    return find_min_helper(g, source, destination, [False]*g.vertices)

def find_min_helper(g, source, destination, visited):
    if source == destination:
        return(0)
    if visited[source]:
        return(-1)

    visited[source] = True

    node = g.array[source].get_head()
    path = -1 

    while node:
        current_path = find_min_helper(g, node.data, destination, visited )
        if current_path > -1:
            if path > -1:
                path = min(1 + current_path, path)
            else:
                path = 1 + current_path
        node = node.next_element
    
    return (path)
'''
graph = {
    0 -> 1
    0 -> 2
    0 -> 3
    3 -> 5
    5 -> 4
    2 -> 4
}
'''

g = Graph(6)
num_of_vertices = g.vertices
if(num_of_vertices == 0):
    print("Graph is empty")
elif(num_of_vertices < 0):
    print("Graph cannot have negative vertices")
else:
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 3)
    g.add_edge(3, 5)   
    g.add_edge(5, 4) 
    g.add_edge(2, 4)

    g.print_graph()

    print(find_min(g,0,4))