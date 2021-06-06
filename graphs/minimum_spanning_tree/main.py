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

    # TODO: Write - Your - Code
    # A minimum spanning tree (MST) or minimum weight spanning tree is a subset of the edges of a connected, edge-weighted undirected graph that connects all the vertices together, without any cycles and with the minimum possible total edge weight
    #
    # MST = 0
    # Mark vertex[0] as Visited
    # while exist non-visited vertices:
    #   select MIN from ( NON VISITED edges from VISITED vertices pointed to NON VISITED vertices )
    #      mark vertice as VISITED
    #      mark edge as VISITED
    #      add cost of EDGE to MST
   
    self.g[0].visited = True
    weight = 0

    while not all([x.visited for x in self.g]):
      visited_vertices = [ x.id for x in self.g if x.visited ]
      #print(f"visited_vertices {visited_vertices}")
      edges = [ e for e in self.e if not e.visited and e.src.id in visited_vertices and e.dest.id not in visited_vertices ]      
      #print(edges)
      min_edge = min(edges,key=lambda x: x.weight)
      min_edge.visited = True
      self.g[min_edge.dest.id - 1].visited = True
      weight+=min_edge.weight


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
    #g.print_graph()
    #print(g.get_graph())

    g.print_mst(g.find_min_spanning_tree())