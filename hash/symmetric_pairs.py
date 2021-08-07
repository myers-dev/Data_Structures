def find_symmetric(my_list):
    s = [ set(i) for i in my_list ]
    r = []
    while s:
        e = s.pop()
        if e in s:
            a = list(e)
            b = [ a[1],a[0] ]
            r.append(a)
            r.append(b)
    return (r)


list1 = [[1, 2], [3, 4], [5, 9], [4, 3], [9, 5]]
print(find_symmetric(list1))