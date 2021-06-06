'''
Output if graph can be classified as
1. Transitive
2. Symmetric
3. Anti-symmetric
4. Asymmetric
5. Reflexive
6. Irreflexive
'''

import sys
sys.path.append('../')

from Graph import Graph
from Queue import MyQueue
from Stack import MyStack

def is_transitive(g):
    '''
    Let A be a set in which the relation R defined
    R is said to be transitive, if
    (a, b) ∈ R and (b, c) ∈ R ⇒ (a, c) ∈ R,
    That is aRb and bRc ⇒ aRc where a, b, c ∈ A.
    '''
    visited = [False] * g.vertices
    stack = MyStack()
    stack.push([None,0])

    while not all(visited):
        #print(stack.stack_list,visited)
        if stack.is_empty():
            stack.push([None,visited.index(False)])
        source, current = stack.pop()
        neighbor = g.array[current].get_head()
        #print(f"  {source}->{current}")
        while neighbor:
            #print(f"     {neighbor.data} {stack.stack_list}")
            # Populating stack
            if not visited[neighbor.data]:
                stack.push([current,neighbor.data])
            # Verifying trainsitivity
            if source is not None:
                if not edge_exist(g,source,neighbor.data):
                    print(f"   Transitivity broken. Edge {source}->{current} and {current}->{neighbor.data} exists but {source}->{neighbor.data}")
                    return False
                else:
                    #print(f"Transitivity verified. Edge {source}->{current} and {current}->{neighbor.data} exists along with {source}->{neighbor.data}")
                    pass
                # Moving to next neighbor
            neighbor = neighbor.next_element
        visited[current] = True
    return True

def edge_exist(g,a,b):
    #print(f"edge_exists(g,{a},{b})")
    node = g.array[a].get_head()
    while node:
        if node.data == b:
            return True
        node = node.next_element
    return False

def is_symmetric(g):
    '''
        If (c,d) is in the relation, then we check whether (d,c) is in the set
    '''
    visited = [False] * g.vertices
    stack = MyStack()
    stack.push([None,0])

    while not all(visited):
        #print(stack.stack_list,visited)
        if stack.is_empty():
            stack.push([None,visited.index(False)])
        source, current = stack.pop()
        neighbor = g.array[current].get_head()
        #print(f"  {source}->{current}")

        #verifying symmetry
        if source is not None:
            if not edge_exist(g, current, source):
                print(f"   Symmetry broken. Edge {source}->{current} exists but {current}->{source}")
                return False
        while neighbor:
            #print(f"     {neighbor.data} {stack.stack_list}")
            # Populating stack
            if not visited[neighbor.data]:
                stack.push([current,neighbor.data])
            neighbor = neighbor.next_element
        visited[current] = True
    return True
    
def is_antisymmetric(g):
    '''
    if R(a, b) and R(b, a), then a = b. Self-loops are allowed
    '''
    visited = [False] * g.vertices
    stack = MyStack()
    stack.push([None,0])

    while not all(visited):
        #print(stack.stack_list,visited)
        if stack.is_empty():
            stack.push([None,visited.index(False)])
        source, current = stack.pop()
        neighbor = g.array[current].get_head()
        #print(f"  {source}->{current}")

        #verifying antisymmetry
        if source is not None:
            if edge_exist(g, current, source) and edge_exist(g, source, current) and current != source:
                print(f"   Anti-Symmetry broken. Edge {source}->{current} exist along with {current}->{source} and {current}!={source}")
                return False
        while neighbor:
            #print(f"     {neighbor.data} {stack.stack_list}")
            # Populating stack
            if not visited[neighbor.data]:
                stack.push([current,neighbor.data])
            neighbor = neighbor.next_element
        visited[current] = True
    return True    

def is_asymmetric(g):
    '''
    A relation R on a set A is called asymmetric if no (y,x) ∈ R when (x,y) ∈ R. 
    Or we can say, the relation R on a set A is asymmetric if and only if, (x,y)∈R⟹(y,x)∉R. 
    '''
    visited = [False] * g.vertices
    stack = MyStack()
    stack.push([None,0])

    while not all(visited):
        #print(stack.stack_list,visited)
        if stack.is_empty():
            stack.push([None,visited.index(False)])
        source, current = stack.pop()
        neighbor = g.array[current].get_head()
        #print(f"  {source}->{current}")

        #verifying asymmetry
        if source is not None:
            if edge_exist(g, current, source) and edge_exist(g, source, current):
                print(f"   Asymmetry broken. Edge {source}->{current} exist along with {current}->{source}")
                return False
        while neighbor:
            #print(f"     {neighbor.data} {stack.stack_list}")
            # Populating stack
            if not visited[neighbor.data]:
                stack.push([current,neighbor.data])
            neighbor = neighbor.next_element
        visited[current] = True
    return True    

def is_reflexive(g):
    '''
    In mathematics, a binary relation R over a set X is reflexive if it relates every element of X to itself.
    '''
    for vertice in range(g.vertices):
        if not edge_exist(g,vertice,vertice):
            print(f"   Reflexivity broken. Edge {vertice}->{vertice} is not exists")
            return False
    return True

def is_irreflexive(g):
    '''
    A relation on a set is irreflexive provided that no element is related to itself; 
    '''
    for vertice in range(g.vertices):
        if edge_exist(g,vertice,vertice):
            print(f"   Irreflexivity broken. Edge {vertice}->{vertice} is exists")
            return False
    return True

def properties(g):
    print("Transitive    : ",is_transitive(g))
    print("Symmetric     : ",is_symmetric(g))
    print("Antisymmetric : ",is_antisymmetric(g))
    print("Asymmetric    : ",is_asymmetric(g))
    print("Reflexive     : ",is_reflexive(g))
    print("Irreflexive   : ",is_irreflexive(g))

graph="""
 0---->1 
  \   /  
   V V   
    2    
"""
print(graph)
g = Graph(3)

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)

properties(g)

graph="""
 0---->1 
  <---- 
    2    
"""
print(graph)
g = Graph(3)

g.add_edge(0, 1)
g.add_edge(1, 0)

properties(g)

graph="""
 0---->1 
  \   /  
   V V   
    2 ----->3
     <-----  
"""
print(graph)
g = Graph(4)

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 2)

properties(g)

graph="""
 
 |-------------|
 |             |
 0---->1       |
  \   /  |     |
   V V    V    |
    2 ----->3<-|
     <-----  
"""
print(graph)
g = Graph(4)

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 2)
g.add_edge(1, 3)
g.add_edge(0, 3)

properties(g)

graph="""
 0---->1 <----><
  <---- 
    2    
"""
print(graph)
g = Graph(3)

g.add_edge(0, 1)
g.add_edge(1, 0)
g.add_edge(1, 1)

properties(g)

graph="""
 0---->1 <----><
    2    
"""
print(graph)
g = Graph(3)

g.add_edge(0, 1)
g.add_edge(1, 1)

properties(g)

graph="""
 ><---->0     1 <----><
    2<----><    
"""
print(graph)
g = Graph(3)

g.add_edge(0, 0)
g.add_edge(1, 1)
g.add_edge(2, 2)

properties(g)