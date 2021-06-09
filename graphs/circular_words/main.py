class vertex: 
  def __init__(self, value, visited):
    self.value = value
    self.visited = visited
    self.adj_vertices = []
    self.in_vertices = []
  
class graph:
  g = []

  def __init__(self, g):
    self.g = g
    
  # This method creates a graph from a list of words. A node of
  # the graph contains a character representing the start or end
  # character of a word.
  def create_graph(self, words_list):
    for i in range(len(words_list)):
      word = words_list[i]
      start_char = word[0]
      end_char = word[len(word) - 1]

      start = self.vertex_exists(start_char)
      
      if start == None:
        start = vertex(start_char, False)
        self.g.append(start)

      end = self.vertex_exists(end_char)
      if end == None:
        end = vertex(end_char, False)
        self.g.append(end)

      # Add an edge from start vertex to end vertex
      self.add_edge(start, end)
    
  # This method returns the vertex with a given value if it
  # already exists in the graph, returns NULL otherwise
  def vertex_exists(self, value):
    for i in range(len(self.g)):
      if self.g[i].value == value:
        return self.g[i]
    return None

  # This method returns TRUE if all nodes of the graph have
  # been visited
  def all_visited(self):
    for i in range(len(self.g)):
      if self.g[i].visited == False:
        return False
    return True

  # This method adds an edge from start vertex to end vertex by
  # adding the end vertex in the adjacency list of start vertex
  # It also adds the start vertex to the in_vertices of end vertex
  def add_edge(self, start, end):
    start.adj_vertices.append(end)
    end.in_vertices.append(start)

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

    # Recursive case
    for i in range(len(adj)):
      if adj[i].visited == False:
        node = adj[i]
        if self.can_chain_words_rec(node, starting_node):
          return True
    return False

  def can_chain_words(self, list_size):
    # Empty list and single word cannot form a chain
    return False
    
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
  g = graph([])
  print(list_of_words)
  g.create_graph(list_of_words)
  # Check for in/out equality
  print("In/Out degrees equality:",g.out_equals_in())

sys.exit()

class verification_tests(unittest.TestCase):

  def test_case1(self):
    g = graph([])
    list_of_words=['eve', 'eat', 'ripe', 'tear']
    g.create_graph(list_of_words)
    self.assertTrue(g.can_chain_words(0))
    
  def test_case2(self):
    g = graph([])
    list_of_words=['aba','aba']
    g.create_graph(list_of_words)
    self.assertTrue(g.can_chain_words(0)) 

  def test_case3(self):
    g = graph([])
    list_of_words=['deg','fed']
    g.create_graph(list_of_words)
    self.assertFalse(g.can_chain_words(0)) 
    
  def test_case4(self):
    g = graph([])
    list_of_words=['ghi', 'abc', 'def', 'xyz']
    g.create_graph(list_of_words)
    self.assertFalse(g.can_chain_words(0))

if __name__ == '__main__':
    unittest.main()