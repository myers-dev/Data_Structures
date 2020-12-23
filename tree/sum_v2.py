from binarytree import Node


def count_paths(root, S):
  return count_paths_recursive(root, S, [])


def count_paths_recursive(currentNode, S, currentPath):

  if currentNode is None:
    return 0

  print("count_paths_recursive called with :",currentNode.val,",",S,",",currentPath)

  # add the current node to the path
  currentPath.append(currentNode.val)
  print("CurrentPath=",currentPath)
  pathCount, pathSum = 0, 0
  # find the sums of all sub-paths in the current path list
  for i in range(len(currentPath)-1, -1, -1):
    pathSum += currentPath[i]
    # if the sum of any sub-path is equal to 'S' we increment our path count.
    if pathSum == S:
      pathCount += 1
    print(f"Checking currentPath[{i}] pathSum={pathSum} pathCount={pathCount}")

  # traverse the left sub-tree
  pathCount += count_paths_recursive(currentNode.left, S, currentPath)
  # traverse the right sub-tree
  pathCount += count_paths_recursive(currentNode.right, S, currentPath)

  # remove the current node from the path to backtrack
  # we need to remove the current node while we are going up the recursive call stack

#  print("CurrnetPath before deleting",currentPath)
#  del currentPath[-1]
#  print("CurrentPath after deleting",currentPath)

  currentPath.pop()

  return pathCount


def main():
  root = Node(12)
  root.left = Node(7)
  root.right = Node(1)
  root.left.left = Node(4)
  root.right.left = Node(10)
  root.right.right = Node(5)

  root.right.left.left = Node(0)

  print(root)
  print("Tree has paths: " + str(count_paths(root, 11)))


main()