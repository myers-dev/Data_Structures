from datetime import datetime

def find_subsets(nums):
  subsets = []

  if len(nums)==0:
    subsets.append([])
  else:
    for subset in find_subsets(nums[1:]):
      if subset not in subsets:
        subsets.append(subset)
      candidate = [nums[0]] + subset
      if candidate not in subsets:
        subsets.append(candidate)
  return(subsets)

def main():

  print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3, 3, 3, 4, 4, 5, 5])))

start = datetime.now()
main()
print(datetime.now() - start)
