from binarytree import Node


def DFS(root,current_path,s):
  if root is None:
    return(0)

  result = 0 
  current_path.append(root.val)
  
  for i in range(len(current_path)-1,-1,-1):
    if sum(current_path[-i:])==s:
        print(current_path[-i:])
        result+=1


  # if root.left is None and root.right is None:
  #   print("!",current_path)
  #   return
  return ( result + DFS(root.left,current_path[:],s) + DFS(root.right,current_path[:],s) )

def main():
  root = Node(-1)
  root.left = Node(7)
  root.right = Node(1)
  root.left.left = Node(3)
  root.right.left = Node(10)
  root.right.right = Node(5)

  root.right.left.left = Node(0)

  print(root)

  print(DFS(root,[],10))


main()