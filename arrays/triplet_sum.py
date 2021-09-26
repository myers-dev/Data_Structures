def search_triplets(arr):
    triplets = []
    arr.sort()
  
    stop = False
    i=0

    while i<len(arr)-2:
        stop = False
        j=i+1
        while not stop and j<len(arr)-1:
            k=j+1
            while k<len(arr):
                print(i,j,k,arr[i] , arr[j] , arr[k],arr[k] + arr[j] + arr[i] )
                if arr[k]<0:
                    print('break!')
                    break
                if arr[k] + arr[j] + arr[i] == 0:
                    triplets.append([arr[k],arr[j], arr[i]])
                    stop = True
                k+=1
            j+=1
        i+=1
    return(triplets)
            
        
arr=[-3, 0, 1, 2, -1, 1, -2]

print (search_triplets(arr))