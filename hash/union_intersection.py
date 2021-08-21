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
# Remove duplicates => list.remove_duplicates()
# Node class  {int data ; Node next_element;}

# Returns a list containing the union of list1 and list2


def union(list1, list2):
    # Write your code here
    r = LinkedList()
    list1.remove_duplicates()
    list2.remove_duplicates()

    d = dict()

    node1 = list1.get_head() if list1.get_head() is not None else list2.get_head()
    node2 = list2.get_head() if list1.get_head() is not None else None

    while node1:
        d[node1.data]=True
        r.insert_at_head(node1.data)
        node1 = node1.next_element

    while node2:
        if node2.data not in d.keys():
            r.insert_at_head(node2.data)
        node2 = node2.next_element

    return (r)

# Returns a list containing the intersection of list1 and list2


def intersection(list1, list2):
    # Write your code here

    r = LinkedList()
    list1.remove_duplicates()
    list2.remove_duplicates()

    d = dict()

    node1 = list1.get_head() if list1.get_head() is not None else list2.get_head()
    node2 = list2.get_head() if list1.get_head() is not None else None

    while node1:
        d[node1.data]=True
        node1 = node1.next_element

    while node2:
        if node2.data in d.keys():
            r.insert_at_head(node2.data)
        node2 = node2.next_element

    return (r)

# Returns a list containing the intersection of list1 and list2


list1 = LinkedList()

list1.insert_at_head(60)
list1.insert_at_head(80)
list1.insert_at_head(20)
list1.insert_at_head(10)

list2 = LinkedList()
list2.insert_at_head(45)
list2.insert_at_head(60)
list2.insert_at_head(30)
list2.insert_at_head(20)
list2.insert_at_head(15)

list1.print_list()
list2.print_list()

print("Union")
union(list1,list2).print_list()

print("Intersection")
intersection(list1,list2).print_list()

