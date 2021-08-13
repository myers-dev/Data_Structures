def find_sub_zero(my_list):
    # Use hash table to store the cumulative sum as a key and
    # the element as the value till which the sum has been calculated
    # Traverse the list and return true if either
    # elem == 0 or sum == 0 or hash table already contains the sum
    # If you completely traverse the list and haven't found any 
    # of the above three conditions, then simply return false
    ht = dict()
    total_sum = 0
    # Traverse through the given list
    for elem in my_list:
        total_sum += elem
        print(f"ht={ht} total_sum={total_sum} elem={elem}")
        if elem is 0 or total_sum is 0 or ht.get(total_sum) is not None:
            return True
        ht[total_sum] = elem
    return False


my_list = [6, 4, -7, 3, 12, 9]
print(my_list)

print(find_sub_zero(my_list))