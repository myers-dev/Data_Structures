def binary_search_rotated(arr, key):
  #TODO: Write - Your - Code
  shift = find_n(arr)

  # performing binary search. 
  # virtual index = index - shift

  vindex = len(arr)//2
  length = len(arr)//2

  index = vindex - shift
  if index < 0:
      index = len(arr) + index

  while arr[index] != key or length < 1:
        length//=2
        if arr[index] < key:
            vindex+=length
        if arr[index] > key:
            vindex-=length
    
        index = vindex - shift
        if index < 0:
            index = len(arr) + index


  if arr[index] == key:
      return(index)
  else:
      return(-1)


def shift(arr, n):
    # shift all elements of array arr by n 
    n = n % len(arr)
    narr = [None]*len(arr)
    for i in range(len(arr)):
        p1 = i
        p2 = i + n if i + n < len(arr) else ( i + n ) - len(arr)
        #print(f"Placing from position {p1} to position {p2}")
        narr[p2] = arr[p1]
    return(narr)

def find_n(arr):
    
    si = 0
    ei = len(arr) - 1

    first = arr[si]
    last = arr[ei]

    while last < first:
        if ei - si == 1 and last < first:
            return (ei)

        # Splitting and and check left and right
        mid = ( si + ei )//2

        if arr[mid] < arr[si]:
            si,ei = si,mid
        elif arr[ei] < arr[mid]:
            si,ei = mid,ei
        else:
            print("Exception")
    
    return(si)
    


arr = [ 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15 ]

print(arr)
for i in range(len(arr)+10):
    narr=shift(arr,i)
    print(i, narr)

    #print(find_n(narr))

    key = 5
    print(binary_search_rotated(arr, key))
        