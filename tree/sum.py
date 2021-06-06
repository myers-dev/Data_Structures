from binarytree import Node
from collections import deque

def paths(path,s):
    count = 0
    for i in range(len(path)):
        sm = path[i]
        if sm == s:
            count+=1
            #print(path[i])
            continue
        for j in range(i+1,len(path)):
            sm+=path[j]
            if sm == s:
                count+=1
                #print(path[i:j+1])
                continue
    return(count)
    
def all_paths(root):
    if root is None:
        return([])   
    nodes = [root]
    paths = [[root.val]]

    while nodes:
        tmp = []
        tmp_paths = []
        #print(paths)
        for idx in range(len(nodes)):
            node = nodes[idx]
            path = paths[idx]
            #print(idx,path)
            if node.left:
                tmp.append(node.left)
                tmp_paths.append( path + [node.left.val] )
            if node.right:
                tmp.append(node.right)
                tmp_paths.append( path + [node.right.val] )    
        nodes = tmp
        paths = tmp_paths if tmp_paths else paths

    return (paths)
                
def return_all_paths(root,s):
    result = 0
    for path in all_paths(root):
        result+=paths(path,s)
    return(result)

if __name__=='__main__':
    root = Node(1)

    root.left = Node(2)
    root.right = Node(2)

    root.left.left = Node(0)
    root.left.right = Node(7)

    root.right.left = Node(4)
    root.right.right = Node(5)


    print(root)
    #print(paths([0,1,2,3,4,5,6,7,8,9,1,8],9))
    print(all_paths(root))
    print(return_all_paths(root,3))

