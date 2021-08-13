#import sys

def find_sub_zero(my_list):
    # Initialize dictionary 
    sdict=dict()
    
    for i1 in range(len(my_list)):
        sdict[(i1,i1)] = my_list[i1]

        for i2 in  range(i1 , len(my_list)):
            if (i1,i2) in sdict.keys():
                s = sdict[(i1,i2)]
            else:
                if (i1,i2 - 1) in sdict.keys():
                    s = my_list[i2] + sdict[(i1, i2 - 1)]
                    sdict[(i1,i2)] = s
                #else:
                    #print("Exception")
                    #sys.exit(1)
            if s == 0:
                #print (f"i1={i1} i2={i2} s={s} my_list={my_list}")
                #print (sdict)
                return(True)
            #else:
                #print (f"i1={i1} i2={i2} s={s} my_list={my_list}")

    return(False)

my_list = [6, 4, -7, 3, 12, 9]
print(find_sub_zero(my_list))