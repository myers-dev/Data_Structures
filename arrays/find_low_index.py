import time

def find_low_index(arr, key):
    shift = len(arr)//2
    pos = shift
    previous = [ pos ]

    while pos >= 0 and pos < len(arr):
        if arr[pos] == key:
            if pos == 0:
                return (pos)
            if arr[pos] == key and arr[pos - 1]!= key:
                return (pos)

        shift = shift // 2 if shift // 2 > 0 else 1
        #print(f"position={pos} shift={shift} previous={previous}")
 
        if arr[pos] < key:
            pos = pos + shift
        else:
            pos = pos - shift

        previous.append(pos)
        if pos == previous[0]:
            return ( -1 )

        if len(previous) == 3:
            previous.pop(0)

    return (-1)

def find_high_index(arr, key):

    shift = len(arr)//2
    pos = shift
    previous = [ pos ]

    while pos >= 0 and pos < len(arr):
        if arr[pos] == key:
            if pos == len(arr) - 1:
                return (pos)
            if arr[pos] == key and arr[pos + 1]!= key:
                return (pos)

        shift = shift // 2 if shift // 2 > 0 else 1
        #print(f"position={pos} shift={shift} previous={previous}")
 
        if arr[pos] <= key:
            pos = pos + shift
        else:
            pos = pos - shift

        previous.append(pos)
        if pos == previous[0]:
            print("!")
            return ( -1 )

        if len(previous) == 3:
            previous.pop(0)

    return (-1)

a=[1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 7, 7, 7, 7, 7, 7]

print(a,len(a))
print (find_low_index(a,5))
print (find_high_index(a,5))
