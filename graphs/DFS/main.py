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

def dfs_traversal_helper(g, source, visited):
    #print(f"Called with {source}")
    result = ""
    stack = MyStack()

    result+=str(source)
    visited[source] = True
    node = g.array[source].get_head()
    while node:
        #print(f"s node={node}")
        stack.push(node)
        node = node.next_element

    while not stack.is_empty():
        node_number = stack.pop().data
        #print (f"visited.keys={visited.keys()},stack.size()={stack.size()},node_number={node_number},result={result}")
        result+=str(node_number)
        if node_number not in visited.keys():
                visited[node_number] = True
                node = g.array[node_number].get_head()

                while node:
                    #print(f"m node.data={node.data}")
                    stack.push(node)
                    node = node.next_element

    #print(len(visited.keys()),len(g.array))
    if len(visited.keys()) < len(g.array):
        for node_number in range(len(g.array)):
            if node_number not in visited.keys():
                result+=dfs_traversal_helper(g,node_number,visited)
    #print(f"Returned {result}")
    return (result)

def dfs_traversal(g, source):
    return ( dfs_traversal_helper(g, source, dict()) )

g = Graph(7)
num_of_vertices = g.vertices
if(num_of_vertices == 0):
    print("Graph is empty")
elif(num_of_vertices < 0):
    print("Graph cannot have negative vertices")
else:
    # g.add_edge(1, 2)
    # g.add_edge(1, 3)
    # g.add_edge(2, 4)
    # g.add_edge(2, 5)
    # g.add_edge(3, 6)

    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 1)
    g.add_edge(2, 3)  
    g.add_edge(3, 2) 
    g.add_edge(3, 1) 
    g.add_edge(3, 4)
    g.add_edge(3, 5)

    # g.print_graph()

    print(dfs_traversal(g, 1))
