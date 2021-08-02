from heapq import *

class SlidingWindowMedian:

  def find_sliding_window_median(self, nums, k):
    result = []
    if len(nums)<k:
        return(result)
    start=0
    while start<=len(nums)-k:
        #print (f"Running starting from {start} ending at {start+k} (not inclusive) {nums} {nums[start:start+k]}")
        h=nums[start:start+k]
        heapify(h)
        #print(f"heap = {h}")
        for i in range(k//2):
            m = heappop(h)
            #print(f"m={m}")
        if k%2 == 0:
            # average
            n = heappop(h)
            #print(f"n={n}")
            result.append((m + n)/2)
        else:
            # median
            result.append(heappop(h))
        start+=1
    
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