def find_pair(my_list):
    sd={}
    for i in range(1,len(my_list)):
        for j in range(0,i):
            #print(i,j)
            s = my_list[i] + my_list[j]
            if s in sd.keys():
                return([sd[s],[my_list[i],my_list[j]]])
            else:
                sd[s]=[my_list[i],my_list[j]]
    return (None)



my_list = [3,4,7,1,12,9]

print(find_pair(my_list))
