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


def remove_duplicates(lst):
    d = dict()
    node = lst.get_head()
    previous = None

    while node:
        #print(f"processing element with data={node.data}, previous={previous}")
        if node.data in d.keys() and previous:
            node = node.next_element
            previous.next_element = node
        else:
            #print("!")
            d[node.data]=True
            previous=node
            node=node.next_element


l = LinkedList()

l.insert_at_head(7)
l.insert_at_head(14)
l.insert_at_head(21)
l.insert_at_head(14)
l.insert_at_head(22)
l.insert_at_head(7)

l.print_list()

remove_duplicates(l)

l.print_list()