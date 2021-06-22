class vertex:                                           # 
  def __init__(self, value, visited):                   #   Class vertex has value ( letter )
    self.value = value                                  #                    visited indicator
    self.visited = visited                              #                    adj_vertices  ?
    self.adj_vertices = []                              #                    in_vertices   ?
    self.in_vertices = []                               #
  
class graph:
  g = []

  def __init__(self, g):
    self.g = g
    
  # This method creates a graph from a list of words. A vertex (self.g[] = value, visited, adj_vertices[], in_vertices[]) of
  # the graph contains a character representing the start or end
  # character of a word.
  # edge is connecting nodes (directed)
  def create_graph(self, words_list):
    for i in range(len(words_list)):
      word = words_list[i]                              # starting from word 0 to last word
      start_char = word[0]                              # start char = first symbol of word
      end_char = word[len(word) - 1]                    # end_car = last symbol

      start = self.vertex_exists(start_char)            # if we created vertex already ( function return ether vertex(self.g[i] ) or None )
      
      if start == None:                                 # so if None - creating new vertex ( letter, not-visited, empty! ad_vertices , empty! in_vertices ),
        start = vertex(start_char, False)               #                        appending vertex to self.g[]
        self.g.append(start)

      end = self.vertex_exists(end_char)                # if we created vertex already ( function return ether vertex(self.g[i] ) or None )
      if end == None:                                   # so if None - creating new vertex ( letter, not-visited, empty! ad_vertices , empty! in_vertices ),
        end = vertex(end_char, False)                   #                        appending vertex to self.g[] 
        self.g.append(end)

      # Add an edge from start vertex to end vertex
      self.add_edge(start, end)                         #    def add_edge(self, start, end):
                                                        #         start.adj_vertices.append(end)   <--- vertex
                                                        #         end.in_vertices.append(start)    <--- vertex
    
  # This method returns the vertex with a given value if it
  # already exists in the graph, returns NULL otherwise
  def vertex_exists(self, value):                       #  Checking if value of letter is exist in self.g
    for i in range(len(self.g)):                        #   If exist , returning the object - vertice
      if self.g[i].value == value:                      #   If not exist , returning None
        return self.g[i]
    return None

  # This method returns TRUE if all nodes of the graph have
  # been visited
  def all_visited(self):                                # If all nodes of the graph has property visited == True -> returning True
    for i in range(len(self.g)):                        # If some of the nodes has property visited == False -> returning False
      if self.g[i].visited == False:
        return False
    return True

  # This method adds an edge from start vertex to end vertex by
  # adding the end vertex in the adjacency list of start vertex
  # It also adds the start vertex to the in_vertices of end vertex
  def add_edge(self, start, end):                       # adj_vertices -> vertice corresponding to the last letter of the word  
    start.adj_vertices.append(end)                      # in_vertices -> vertice corresponding to the first letter of the word
    end.in_vertices.append(start)                       # Example [ eve, eat, ripe,tear ]
                                                        #      e            t       r
                                                        # adj: ['e', 't']   ['r']   ['e']
                                                        # in : ['e', 'r']   ['e']   ['t']

                                                        # ┌───┐
                                                        # │   │
                                                        # │   │
                                                        # └─► E
                                                        #      ◄─────R
                                                        #     │       ▲
                                                        #     └─► T───┘

# How to check if a directed graph is eulerian?
# A directed graph has an eulerian cycle if following conditions are true (Source: https://tutorialspoint.dev/data-structure/graph-data-structure/euler-circuit-directed-graph)
# 1) All vertices with nonzero degree belong to a single strongly connected component.
# 2) In degree and out degree of every vertex is same.

# We can detect singly connected component using Kosaraju’s DFS based simple algorithm.
# To compare in degree and out degree, we need to store in degree an out degree of every vertex. <-- already done !
# Out degree can be obtained by size of adjacency list. In degree can be stored by creating an array of size equal to number of vertices.

# Kosaraju's algorithm
# https://www.geeksforgeeks.org/strongly-connected-components/
#
# 1. Create an empty stack ‘S’ and do DFS traversal of a graph. 
#     In DFS traversal, after calling recursive DFS for adjacent vertices of a vertex, push the vertex to stack
# 2. Reverse directions of all arcs to obtain the transpose graph. ( change adj to in , in to adj)
# 3. One by one pop a vertex from S while S is not empty. Let the popped vertex be ‘v’. 
#     Take v as source and do DFS (call DFSUtil(v)). The DFS starting from v prints strongly connected component of v.




  # This method returns TRUE if out degree of each vertex is equal
  # to its in degree, returns FALSE otherwise
  def out_equals_in(self):
    for i in range(len(self.g)):
      out = len(self.g[i].adj_vertices)
      inn = len(self.g[i].in_vertices)
      if out != inn:
        return False
    return True

  # This method returns TRUE if the graph has a cycle containing
  # all the nodes, returns FALSE otherwise
  def can_chain_words_rec(self, node, starting_node):

    
    node.visited = True

    # Base case
    # return TRUE if all nodes have been visited and there
    # exists an edge from the last node being visited to
    # the starting node
    adj = node.adj_vertices
    if self.all_visited():
      for i in range(len(adj)):
        if adj[i] == starting_node:
          return True
    print("node.value=",node.value,"node.adj_vertices()=",[ x.value for x in node.adj_vertices ])

    # Recursive case
    for i in range(len(adj)):
      if adj[i].visited == False:
        node = adj[i]
        if self.can_chain_words_rec(node, starting_node):
          return True
    print("returning False","node.value=",node.value,"node.adj_vertices()=",[ x.value for x in node.adj_vertices ])
    return False

  def can_chain_words(self, list_size):
    # Empty list and single word cannot form a chain

    # 1. Verifying if all nodes belongs to strongly connected component
    # 2. Verifying if in degrees and out degrees are the same

    return (False)
    
  def print_graph(self):
    for i in range(len(self.g)):
      print(self.g[i].value + " " + str(self.g[i].visited) + "\n")
      adj = self.g[i].adj_vertices
      for j in range(len(adj)):
        print(adj[j].value + " ")
      print("\n")

import unittest
import sys

for list_of_words in [ ['eve', 'eat', 'ripe', 'tear'] , ['aba','aba'] , ['deg','fed'] , ['ghi', 'abc', 'def', 'xyz'] ]:
  word = graph([])
  print(list_of_words)
  word.create_graph(list_of_words)
  for element in word.g:
    print(f"Value {element.value}")
    print(f"   adj: {[x.value for x in element.adj_vertices]}")
    print(f"   in : {[x.value for x in element.in_vertices]}")
  
  print(word.can_chain_words_rec(word.g[0],0))
  sys.exit()
  # Check for in/out equality
  print("In/Out degrees equality:",g.out_equals_in())

sys.exit()

class verification_tests(unittest.TestCase):

  def test_case1(self):
    g = graph([])
    list_of_words=['eve', 'eat', 'ripe', 'tear']
    g.create_graph(list_of_words)
    self.assertTrue(g.can_chain_words_rec(0))
    
  def test_case2(self):
    g = graph([])
    list_of_words=['aba','aba']
    g.create_graph(list_of_words)
    self.assertTrue(g.can_chain_words_rec(0)) 

  def test_case3(self):
    g = graph([])
    list_of_words=['deg','fed']
    g.create_graph(list_of_words)
    self.assertFalse(g.can_chain_words_rec(0)) 
    
  def test_case4(self):
    g = graph([])
    list_of_words=['ghi', 'abc', 'def', 'xyz']
    g.create_graph(list_of_words)
    self.assertFalse(g.can_chain_words_rec(0))

if __name__ == '__main__':
    unittest.main()