from typing import Sized


class vertice:

    def __init__(self,id):

        self.id = None

        self.neighbors = [] # array with id of the neighbors ( e.g. [ 1,3,5 ] )
        
        self.indegree = 0
        self.inpath = False

class graph:

    def __init__(self,size):

        self.vertices = [ vertice(id) for id in range(size) ] # array with vertices = contains vertice id , indegree, inpath for vertice and edge

    def insert(self,sd):
        source,destination = sd

        self.vertices[source].neighbors.append(destination)

        self.vertices[destination].indegree+=1

        if not self.vertices[source].id:
            self.vertices[source].id = source
        if not self.vertices[destination].id:
            self.vertices[destination].id = destination


    def mark_vertice_inpath(self,id):
        self.vertices[id].inpath = True
        for n in self.vertices[id].neighbors:
            if not self.vertices[n].inpath:
                self.vertices[n].indegree-=1

    def unmark_vertice_inpath(self,id):
        self.vertices[id].inpath = False
        for n in self.vertices[id].neighbors:
            if not self.vertices[n].inpath: 
             self.vertices[n].indegree+=1

    def display_graph(self):
        
        for v in range(len(self.vertices)):
            print(f"Vertice: {v} Indegree: {self.vertices[v].indegree}, {self.vertices[v].inpath} -> ")
            for n in self.vertices[v].neighbors:
                print(f"               {n} {self.vertices[n].inpath}")
    
    def dfs_traversal(self):
        # DFS traversal ( recursive ), storing output, merging and returning all paths
        # making the stack of all vertices with indegree == 0:
        #print("Starting...")
        #self.display_graph()
        stack = []
        for v in self.vertices:
            if v.indegree == 0 and not v.inpath:
                stack.append(v)
                #print(f"Found vertice {v.id} with indegree of 0 and not inpath")
        #print (f"Stack {[v.id for v in stack]}")
        # check for compliance

        return_path = []

        if len(stack) == 0 and not all([v.inpath for v in self.vertices]):
            #print("Something wrong with a graph, could not find the vertices with indegree of 0. Also we still have unvisited vertices ")
            #self.display_graph()
            return(False)
            
        # stack is healthy, working it

        for v in stack:
            # Marking v as inpath
            self.mark_vertice_inpath(v.id)
            #print (f"before calling self.dfs_traversal() v={v.id} from stack={[x.id for x in stack]} here are how our graph looks like:")
            #self.display_graph()
            paths = self.dfs_traversal()
            #print(f"v={v.id} from stack={[x.id for x in stack]} paths={paths}")
            if len(paths)<1:
                return_path.append([v.id])
            else:
                for path in paths:
                    return_path.append([v.id] + path)
                    
            self.unmark_vertice_inpath(v.id)
        #print(f"return_path={return_path}")
        return (return_path)


def print_orders(tasks, prerequisites):
    # populating graph
    g = graph(tasks)
    for p in prerequisites:
        g.insert(p)
    
    #g.display_graph()

    paths = g.dfs_traversal()
    #print(f"Here is a final result : {paths}")
    for path_id in range(len(paths)):
        if len(paths[path_id]) == tasks:
            print(f"{path_id + 1} {paths[path_id]}")

def main():
  print("Task Orders: ")
  print_orders(3, [[0, 1], [1, 2]])

  print("Task Orders: ")
  print_orders(4, [[3, 2], [3, 0], [2, 0], [2, 1]])

  print("Task Orders: ")
  print_orders(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])


main()