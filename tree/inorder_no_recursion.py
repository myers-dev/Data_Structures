from binarytree import tree, bst, heap, Node

def inorder(root):
    left_stack = [root]
    right_stack = []

    result=[]

    while left_stack or right_stack:
        #print (f"left stack {left_stack}")
        #print (f"right stack {right_stack}")
        if left_stack:
            node = left_stack.pop()
            right_stack.append(node)
            if node.left:
                left_stack.append(node.left)
        else:
            node = right_stack.pop()
            result.append(node.val)
            if node.right:
                left_stack.append(node.right)
    return(result)

if __name__=='__main__':

    root = Node(10)

    root.left = Node(5)
    root.right = Node(15)

    root.left.left = Node(3)
    root.left.right = Node(7)
   
    root.left.right.left = Node(6)
    root.left.right.right = Node(8)

    root.left.left.left = Node(1)
    root.left.left.right = Node(4)

    root.right.right = Node(20)
    root.right.left = Node(12)

    root.right.right.right = Node(25)
    root.right.right.left = Node(18)

    print(root)

    print(inorder(root))