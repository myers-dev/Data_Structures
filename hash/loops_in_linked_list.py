import sys
sys.path.append('./LinkedList')

from LinkedList import LinkedList
from Node import Node
# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Delete at head => list.delete_at_head()
# Delete by value => list.delete(value)
# Search for element => list.search()
# Length of the list => list.length()
# Node class  { int data ; Node next_element;}


def detect_loop(lst):
    d = dict()
    node = lst.get_head()
    while node:
        if node.data in d.keys():
            return (True)
        d[node.data] = True
        node=node.next_element

    return (False)

l = LinkedList()

l.insert_at_head(6)
l.insert_at_head(10)
l.insert_at_head(9)
l.insert_at_head(4)
l.insert_at_head(6)

l.print_list()

print(detect_loop(l))