'''
This is an implementatin of finding the Median of a Number Stream that using two heaps
I included basic verification that storing the stream in the list and calculate median in 
brute-forse way

max_heap using min_heap implementatin with negative numbers
https://stackoverflow.com/questions/2501457/what-do-i-use-for-a-max-heap-implementation-in-python

'''

from heapq import heappush,heappop
from random import randint

class NumberStream:
    def __init__(self):
        self.min_heap = [] # with negatives !
        self.max_heap = [] # with normal numbers

        # Legacy, using sort every time
        self.stream = []


    def add(self,n):
        # Updating legacy
        self.stream.append(n)
        # Updating heaps
        # Where to put it ? we have maximum of minimums and minimum of maximums
        # Comparing it to "maximum of minimums" and "minimum of maximums"
        # (n) (max_of_min) (n) (min_of_max) (n)
        
        if len(self.min_heap)==0:
            heappush(self.min_heap,-n)
            return

        if n <= -self.min_heap[0]:
            heappush(self.min_heap,-n)
        else:
            heappush(self.max_heap,n)

        # Rebalancing heaps
        while len(self.min_heap) - len(self.max_heap) > 1:
            heappush(self.max_heap,-heappop(self.min_heap))
        
        while len(self.max_heap) - len(self.min_heap) > 0:
            heappush(self.min_heap,-heappop(self.max_heap))
        

    def get_median(self):
        # length of heaps are the same
        if len(self.min_heap) == len(self.max_heap):
            return (self.max_heap[0] - self.min_heap[0])/2
        # length of min_heap one more than max_heap
        return (-self.min_heap[0])

    def get_median_legacy(self):
        if len(self.stream)%2 == 1:
            # return median
            return sorted(self.stream)[len(self.stream)//2]
        else:
            # return average
            a = sorted(self.stream)[len(self.stream)//2-1]
            b = sorted(self.stream)[len(self.stream)//2]
            return ((a+b)/2)

if __name__ =='__main__':
    stream = NumberStream()
    for _ in range(100):
        stream.add(randint(0,100))
        #print(sorted(stream.stream))
        print(stream.get_median(),stream.get_median_legacy())