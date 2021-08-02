from MinHeap import MinHeap


def findKSmallest(lst, k):
    heap = MinHeap()  # Create a minHeap
    # Populate the minHeap with lst elements
    heap.buildHeap(lst)
    # Create a list of k elements such that:
    # It contains the first k elements from
    # removeMin() function
    kSmallest = [heap.removeMin() for i in range(k)]
    return kSmallest


lst = [9, 4, 7, 1, -2, 6, 5]
k = 3
print(findKSmallest(lst, k))
