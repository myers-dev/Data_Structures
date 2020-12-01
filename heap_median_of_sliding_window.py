
class SlidingWindowMedian:
  def __init__(self):
      self.min_heap = []
      self.max_heap = []

  def heapify_down(self,heap,idx):
    swap = True
    while swap:
      swap = False
      minimum = None
      if (2*idx + 1) < len(heap) and heap[2*idx + 1] < heap[idx]:
        minimum = 2 * idx + 1
      if (2*idx + 2) < len(heap) and heap[2*idx + 2] < heap[idx]:
        minimum = 2 * idx + 2      
      if minimum:
        swap = True
        heap[idx],heap[minimum] = heap[minimum],heap[idx]
        idx = minimum
      
  def find_sliding_window_median(self, nums, k):
    heap = []

    for i in range(len(nums) - k - 1):
      if not heap:
        heap = heapify(i,i+k)
      

    result = []
    # TODO: Write your code here
    return result

def main():

  slidingWindowMedian = SlidingWindowMedian()
  result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 2)
  print("Sliding window medians are: " + str(result))

  slidingWindowMedian = SlidingWindowMedian()
  result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 3)
  print("Sliding window medians are: " + str(result))


main()
