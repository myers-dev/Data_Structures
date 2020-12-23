#!/usr/bin/python3

from binarytree import tree, bst, heap, Node

def inorder(root,traversal=[]):
    if root is None:
        return None
    if root.left:
        inorder(root.left)
    traversal.append(root.value)
    if root.right:
        inorder(root.right)
    return(traversal)

if __name__=='__main__':
    root = Node(1)

    root.left = Node(2)
    root.right = Node(3)

    root.right.left = Node(4)
    root.right.right = Node(5)


    print(root)

    print(inorder(root))

