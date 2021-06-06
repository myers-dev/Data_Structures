
class SlidingWindowMedian:
  def __init__(self):
      self.heap = []

  def heapify_down(self,idx):
    swap = True
    while swap:
      swap = False
      minimum = None
      if (2*idx + 1) < len(self.heap) and self.heap[2*idx + 1] < self.heap[idx]:
        minimum = 2 * idx + 1
      if (2*idx + 2) < len(self.heap) and self.heap[2*idx + 2] < self.heap[idx]:
        minimum = 2 * idx + 2      
      if minimum:
        swap = True
        self.heap[idx],self.heap[minimum] = self.heap[minimum],self.heap[idx]
        idx = minimum
    
  def heapify_up(self,idx):
    swap = True
    while swap:
      swap = False
      #print(idx,self.heap)
      if idx>0 and self.heap[idx//2] > self.heap[idx]:
        swap = True
        self.heap[idx//2],self.heap[idx] = self.heap[idx],self.heap[idx//2]
        idx = idx//2
  
  def remove_element(self,element):
    # swapping element with last, heapify down
    idx = self.heap.index(element)
    if idx == len(self.heap) - 1:
      return(self.heap.pop())
    result,self.heap[idx] = self.heap[idx],self.heap.pop()
    self.heapify_down(idx)
    return(result)

  def pop_min(self):
    if len(self.heap) == 1:
      return(self.heap.pop())
    else:
      result = self.heap[0]
      self.heap[0] = self.heap.pop()
      self.heapify_down(0)
    return(result)

  def add_element(self,element):
    self.heap.append(element)
    self.heapify_up(len(self.heap) - 1)

  def find_sliding_window_median(self, nums, k):
    if k == 1:
      return(nums)

    medians = []

    for i in range(len(nums) - k + 1):
      sorted_list = []
      for idx in range(i,i+k):
        self.add_element(nums[idx])
      #print(k,self.heap)
      for idx in range(len(self.heap)):
        sorted_list.append(self.pop_min())
      #print(sorted_list)
      if len(sorted_list)%2 == 1:
        medians.append(sorted_list[len(sorted_list)//2 ])
      else:
        medians.append((sorted_list[len(sorted_list)//2 - 1] + sorted_list[len(sorted_list)//2])/2)
    return(medians)

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
