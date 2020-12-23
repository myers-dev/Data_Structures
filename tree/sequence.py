from binarytree import Node

def find_path(root,sequence):
    if len(sequence) == 0:
        return False
    if root is None:
        return False

    if root.val != sequence[0]:
        return False
    if len(sequence) == 1:
        return True
    left, right = False, False
    if root.left:
        left = find_path(root.left,sequence[1:])
    if root.right:
        right = find_path(root.right,sequence[1:])
    
    return (left or right)

if __name__=='__main__':
    root = Node(1)

    root.left = Node(2)
    root.right = Node(2)

    root.left.left = Node(0)
    root.left.right = Node(7)

    root.right.left = Node(4)
    root.right.right = Node(5)


    print(root)

    print(find_path(root,[1,2,4]))