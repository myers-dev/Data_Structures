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

    def topological_sort(self):

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

def find_order(tasks, prerequisites):
    # Edge Cases
    # Walking over the array , building graph of dependencies; 
    # Checking if cycles exist


    g = graph()
    for (source,destination) in prerequisites:
        g.insert(source,destination)

    return (g.topological_sort())

def main():
  print("Is scheduling possible: " + str(find_order(3, [[0, 1], [1, 2]])))
  print("Is scheduling possible: " +
        str(find_order(3, [[0, 1], [1, 2], [2, 0]])))
  print("Is scheduling possible: " +
        str(find_order(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])))

main()