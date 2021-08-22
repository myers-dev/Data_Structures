def find_max_sliding_window(arr, window_size):
  result = []
  i = 0
  while i <= len(arr) - window_size:
      result.append(max(arr[i:i+window_size]))
      i+=1
  return (result)

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
print ("Array = " + str(array))
print ("Max = " + str(find_max_sliding_window(array, 3)))

array = [10, 6, 9, -3, 23, -1, 34, 56, 67, -1, -4, -8, -2, 9, 10, 34, 67]  
print ("Array = " + str(array))
print ("Max = " + str(find_max_sliding_window(array, 3)))