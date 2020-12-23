#!/usr/bin/python3

from binarytree import tree, bst, heap, Node

def pre_order(root,traversal=[]):
    if root is None:
        return None
    traversal.append(root.value)
    if root.left:
        pre_order(root.left)
    if root.right:
        pre_order(root.right)
    return(traversal)

if __name__=='__main__':
    root = Node(1)

    root.left = Node(2)
    root.right = Node(3)

    root.right.left = Node(4)
    root.right.right = Node(5)


    print(root)

    print(pre_order(root))

