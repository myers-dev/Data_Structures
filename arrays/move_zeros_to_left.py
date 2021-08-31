def move_zeros_to_left(A):
    count=0
    l=len(A)
    for i in range(l - 1,-1,-1):
        if A[i] == 0:
            count+=1
        else:
            # Moving element from position i to i + count 
            #print(f"Moving element from position {i} -> {A[i]} to position { i + count }")
            A[i + count ] = A[i]
        
    for i in range(count):
        A[i]=0
    return(A)

A=[1,10,20,0,59,63,0,88]

print(A)
print (move_zeros_to_left(A))