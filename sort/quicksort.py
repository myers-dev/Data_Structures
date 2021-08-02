from random import randint
import sys

def quickSort(lst,start,stop,debug = 0):
    if start < stop :
        pi = partition(lst,start,stop,debug=debug)
        if debug:
            print (f"pi={pi}, start={start}, stop={stop}")

        quickSort(lst, start, pi -1,debug=debug)
        quickSort(lst, pi + 1, stop,debug=debug)
    return(lst)

def partition(lst,start,stop,algo=1,debug=0):
    if (stop - start )<2:
        return (start)
    # Pivot selection :
    #    1. Always select first element as a pivot
    #    2. Always select last element as a pivot
    #    3. Always select random element as a pivot
    #    4. Always select median as a pivot

    #if debug:
    #    print(f"Debug: start={start}, stop={stop}, lst={lst}, algo={algo}")
    if algo==1:
        pivot_loc = start
    elif algo==2:
        pivot_loc = stop
    elif algo==3:
        pivot_loc=randint(start,stop)
    else:
        pivot_loc=int(start+(stop-start)/2)

    pivot_value = lst[pivot_loc]
    left = start - 1

    for index in range(start,stop - 1 ):
        #if debug:
        #    print(f"Debug: index={index} pivot_loc={pivot_loc} pivot_value={pivot_value}")
        if index != pivot_loc:
            if lst[index] < pivot_value:
                if debug:
                    print(f"Debug: Moving: index={index} to the right side of the left={left}, lst={lst}, algo={algo}")

                left+=1
                lst[left],lst[index] = lst[index],lst[left]
                
                if debug:
                    print(f"Debug: Moved: index={index} to the right side of the left={left}, lst={lst}, algo={algo}")
                #sys.exit(1)
    lst[left + 1] , lst[pivot_loc] = lst[pivot_loc] , lst[left + 1]

    #if debug:
    #    print(f"Debug: start={start}, stop={stop}, lst={lst}, algo={algo}, pivot_loc={pivot_loc}, pivot_value={pivot_value}")   

    return ( left + 1 )

    
if __name__=='__main__':
    lst = [1,9,2,8,3,7,4,6,5]
    print ( lst )
    print ( quickSort(lst,0, len(lst),debug=1) )
