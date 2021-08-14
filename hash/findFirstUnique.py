def findFirstUnique(lst):
    d=dict()
    for n in lst:
        if n not in d.keys():
            d[n]=1
        else:
            d[n]+=1
    for n in lst:
        if d[n]==1:
            return(n)
    return (False)    

lst=[9,2,3,2,6,6]
print (findFirstUnique(lst))