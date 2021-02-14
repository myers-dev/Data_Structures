class Node:
  def __init__(self, d):
    self.data = d
    self.neighbors = []

def clone(root):
    d = {} # using the dictionary to store old->new mapping and to track if node is processed
    s = [] # using the stack to keep track of nodes we are going through

    d[root] = Node(root.data)

    s.append(root)

    while s:
        node = s.pop()
        node_copy = d[node]
        for neighbor in node.neighbors:
            if neighbor not in d:
                d[neighbor] = Node(neighbor.data)
                s.append(neighbor)
            node_copy.neighbors.append(d[neighbor])
    return(d[root])