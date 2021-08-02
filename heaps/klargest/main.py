from MaxHeap import MaxHeap


def findKLargest(lst, k):
    # Write your code here
    h=MaxHeap()
    for e in lst:
        h.insert(e)
    return([h.removeMax() for i in range(k)])
