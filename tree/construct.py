from binarytree import Node
from inorder import inorder
from pre_order import pre_order

def construct(i,p):
    if not i or not p:
        return None

    root_value = p[0]
    root = Node(root_value)

    for idx in range(len(i)):
        if i[idx]==root_value:
            break
    len_left = idx
    len_right = len(i) - 1 - idx

    # print("--------")
    # print("i=",i,"p=",p)
    # print("len_left = ",len_left,"len_right=",len_right)
    # print("root.left = ",i[:idx],p[1: len_left + 1])
    # print("root.right = ",i[idx+1:],p[-len_right:])

    root.left = construct(i[:idx],p[1: len_left + 1])

    root.right = construct(i[idx+1:],p[-len_right:])

    return(root)

if __name__=='__main__':
    root = Node(1)

    root.left = Node(2)
    root.right = Node(3)

    root.right.left = Node(4)
    root.right.right = Node(5)


    print(root)

    i = inorder(root)
    p = pre_order(root)

    print(i,p)
    print(construct(i,p))