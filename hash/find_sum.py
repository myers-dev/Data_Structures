def findSum(lst, k):
    h = dict()
    for n in lst:
        h[n]=True
    for n in lst:
        if (k - n) in h.keys():
            return([n,k-n])
    return (False)

lst = [1,21,3,14,5,60,7,6]
k = 81

print (findSum(lst,k))