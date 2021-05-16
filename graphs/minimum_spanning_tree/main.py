class vertex:
  def __init__(self, id, visited):
    self.id = id
    self.visited = visited

class edge:
  def __init__(self, weight, visited, src, dest):
    self.weight = weight
    self.visited = visited
    self.src = src
    self.dest = dest

class graph:
  g = []    #vertices
  e = []    #edges

  def __init__(self, g, e):
    self.g = g
    self.e = e

  # This method returns the vertex with a given id if it
  # already exists in the graph, returns NULL otherwise
  def vertex_exists(self, id):
    for i in range(len(self.g)):
      if self.g[i].id == id:
        return self.g[i]
    return None

  # This method generates the graph with v vertices
  # and e edges
  def generate_graph(self, vertices, edges):
    # create vertices
    for i in range(vertices):
      v = vertex(i + 1, False)
      self.g.append(v)

    # create edges
    for i in range(len(edges)):
      src = self.vertex_exists(edges[i][1])
      dest = self.vertex_exists(edges[i][2])
      e = edge(edges[i][0], False, src, dest)
      self.e.append(e)


  def find_min_spanning_tree(self):
    weight = -1
    # TODO: Write - Your - Code
    #
    # Going over all neighbors ( BFS )
    # Add first node to queue
    # queue not empty ?
    #   pick element from queue
    #     go over all neighbors
    #         edge is visited ?
    #         not ? weight of edge to reach neighbor = current weight + weight of edge
    #         yes ? 
    #           Compare weight to reach neighbor with existing; 
    #             If new weight is smaller than 
    #                 update weight
    #                 update neighbor as not visited
    #                 add neighbor veritce to queue
    #             Else
    #                do nothing
    # 
    # Calculate and return the sum
    stack = [ self.g[0] ]

    while stack:
      current = stack.pop()
      print(f"Popped {current} stack {stack}")



    return weight

  def print_graph(self):
    for i in range(len(self.g)):
      print(str(self.g[i].id) + " " + str(self.g[i].visited) + "\n")

    for i in range(len(self.e)):
      print(str(self.e[i].src.id) + "->" + str(self.e[i].dest.id) + "[" + str(self.e[i].weight) + ", " + str(self.e[i].visited) + "]  ")

    print("\n")
    
  def get_graph(self):
    res = ""
    for i in range(len(self.e)):
      if(i == len(self.e)-1):
        res += "[" + str(self.e[i].src.id) + "->" + str(self.e[i].dest.id) + "]"
      else:
        res += "[" + str(self.e[i].src.id) + "->" + str(self.e[i].dest.id) + "],"    
    return res
  

  def print_mst(self,w):
    print("MST")
    for i in range(len(self.e)):
      if self.e[i].visited == True:
        print(str(self.e[i].src.id) + "->"
            + str(self.e[i].dest.id))

    print("weight: " + str(w))
    print("\n")


if __name__ == "__main__":
    
    vertices = 5
    edges = [[1,1,2],
            [1,1,3],
            [2,2,3],
            [3,2,4],
            [2,4,5],
            [3,3,5]]    
    g = graph([],[])
    g.generate_graph(vertices,edges)
    g.print_graph()
    print(g.get_graph())

    g.print_mst()