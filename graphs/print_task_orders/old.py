class vertice:  
    def __init__(self, value):
        self.value = value
        self.indegree = 0

        self.visited = False
        self.inpath = False # for Cycle detection ( https://algotree.org/algorithms/tree_graph_traversal/depth_first_search/cycle_detection_in_directed_graphs)

class graph:

    def __init__(self):
        self.edges = {} # dictionary ; key is the vertice; value - list of outgoing adjacencies

    def insert(self,value,adj_value):
        if not self.vertice_exist(value):
            source = vertice(value)
            self.edges[source]=[]
        else:
            source = [ v for v in self.edges.keys() if v.value == value ][0]
            
        if not self.vertice_exist(adj_value):
            destination = vertice(adj_value)
            self.edges[destination]=[]
        else:
            destination = [ v for v in self.edges.keys() if v.value == adj_value ][0]

        self.edges[source].append(destination)
        destination.indegree+=1

        return

    def topological_order(self):

        out = [] # array of topological order
        stack = [] # operational stack for bfs

        while self.edges.keys():
            for v in self.edges.keys():
                if v.indegree == 0:
                    stack.append(v)
            if not stack:
                return False # No vertices with indegree of 0
            while stack:
                v = stack.pop()

                while self.edges[v]:
                    neighbor = self.edges[v].pop()

                    neighbor.indegree-=1

                    if neighbor.indegree==0:
                        stack.append(neighbor)

                del self.edges[v]
                out.append(v.value)
        
        return (out)
       
    def vertice_exist(self,value):
        if value in [v.value for v in self.edges.keys()]:
            return True
        return False

# TBD here <----    

def print_orders(tasks, prerequisites):

    g = graph()
    for (source,destination) in prerequisites:
        g.insert(source,destination)

    for o in g.topological_order():
        print(o)
        
    return

def main():
  print("Task Orders: ")
  print_orders(3, [[0, 1], [1, 2]])

  print("Task Orders: ")
  print_orders(4, [[3, 2], [3, 0], [2, 0], [2, 1]])

  print("Task Orders: ")
  print_orders(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])


main()
