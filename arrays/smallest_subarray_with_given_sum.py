def smallest_subarray_with_given_sum(s, arr):
    print(s,arr)

    current_min_length=0
    
    index1=0
    current_sum = arr[index1]
    index2=index1

    while index1<len(arr) and index2<len(arr):
        if current_sum>=s:
            if current_min_length==0 or current_min_length>(index2 - index1 + 1):
                current_min_length=index2 - index1 + 1
            current_sum-=arr[index1]
            index1+=1
            if index2<index1:
                index2=index1
                if index2<len(arr):
                    current_sum=arr[index1]
        else:    
            index2+=1
            if index2<len(arr):
                current_sum+=arr[index2]
    return(current_min_length)    
    
    
    
a=[2, 1, 5, 1, 3, 2]
s=7

print("Min length=",smallest_subarray_with_given_sum(s,a))

a=[2,1,5,2,8]
s=7
 
print("Min length=",smallest_subarray_with_given_sum(s,a))
