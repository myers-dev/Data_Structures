def is_disjoint(list1, list2):
    s = set(list1)
    for e in list2:
        if e in s:
            return (False)
    return (True)


list1 = [9,4,3,1,-2,6,5]
list2 = [7,10,8]

print(is_disjoint(list1,list2))