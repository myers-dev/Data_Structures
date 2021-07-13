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

def find_order(w):
    # populating graph
    #print(w)
    d = {b:a for (a,b) in enumerate(set("".join(w)))}
    rd = { d[a]:a for a in d }

    #print(d)
    g = graph(len(d))

    for i in range(len(w) - 1):
        for j in range(min(len(w[i]),len(w[i+1]))):
            if w[i][j] != w[i+1][j]:
                
                src = d[w[i][j]]
                dst = d[w[i+1][j]]
                
                #print(w[i][j],'->',w[i+1][j],[src,dst])
                g.insert([src,dst])
                break

    #g.display_graph()

    paths = g.dfs_traversal()
    #print(f"Here is a final result : {paths}")
    for path_id in range(len(paths)):
        print(w," ".join([ rd[l] for l in paths[path_id] ])  )

    return("")

def main():
  print("Character order: " + find_order(["ba", "bc", "ac", "cab"]))
  print("Character order: " + find_order(["cab", "aaa", "aab"]))
  print("Character order: " + find_order(["ywx", "wz", "xww", "xz", "zyy", "zwz"]))


main()

