def make_squares(arr):

    squares = []
    
    index1=len(arr) - 1
    index2=0

    while len(squares) < len(arr):
        if arr[index1]**2 > arr[index2]**2:
            squares.insert(0,arr[index1]**2)
            index1-=1
        else:
            squares.insert(0,arr[index2]**2)
            index2+=1
    
    return(squares)


print(make_squares([-2, -1, 0, 2, 3]))