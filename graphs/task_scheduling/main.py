class vertice:  
    def __init__(self, value):
        self.value = value
        self.visited = False
        self.inpath = False # for Cycle detection ( https://algotree.org/algorithms/tree_graph_traversal/depth_first_search/cycle_detection_in_directed_graphs)

class graph:

    loop_exist = False

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
        
    def vertice_exist(self,value):
        if value in [v.value for v in self.edges.keys()]:
            return True
        return False

    def detect_loop_helper(self):
        self.detect_loop(list(self.edges.keys())[0])

    def detect_loop(self,start):
        # DFS
        start.visited = True
        start.inpath = True

        #print(self.edges[start])

        for neighbor in self.edges[start]:
                
                #print([n.inpath for n in self.edges[neighbor]])
                if any([n.inpath for n in self.edges[neighbor]]):
                    #print("Loop detected")
                    self.loop_exist = True
                    return 
                elif not neighbor.visited:
                    self.detect_loop(neighbor)
        # Before we backtrack unset the flag for the src vertex as it
        # might be in the next traversal path
        start.inpath = False
        
        return    
        
def is_scheduling_possible(tasks, prerequisites):
    # Edge Cases
    # Walking over the array , building graph of dependencies; 
    # Checking if cycles exist


    g = graph()
    for (source,destination) in prerequisites:
        g.insert(source,destination)

    g.detect_loop_helper()

    if not g.loop_exist:
        return True
    
    return False

def main():
  print("Is scheduling possible: " +
        str(is_scheduling_possible(3, [[0, 1], [1, 2]])))
  print("Is scheduling possible: " +
        str(is_scheduling_possible(3, [[0, 1], [1, 2], [2, 0]])))
  print("Is scheduling possible: " +
        str(is_scheduling_possible(6, [[0, 4], [1, 4], [3, 2], [1, 3]])))

main()