import math

def triplet_sum_close_to_target(arr, target_sum):
    #print(f"arr={arr} target_sum={target_sum}")
    arr.sort()
    candidate = None  

    for i in range(len(arr) - 2):
        for j in range(i + 1, len(arr) - 1):
            f = j + 1
            #print(f"i={i} j={j}")
            while f<len(arr) and f>j:
                current = arr[i] + arr[j] + arr[f]
                #print(f"i={i} j={j} f={f} current={current} candidate={candidate}")
                if candidate is None:
                    candidate = current
                elif abs(current - target_sum) < abs(candidate - target_sum) :
                    candidate = current
                    adjust = int(math.ceil(( len(arr) - 1 ) - f )/2)
                    if adjust == 0:
                        break
                    f+=adjust
                else:
                    adjust = int(math.ceil(( f - j + 1 )/2))
                    if adjust == 0:
                        break
                    f-=adjust




    # TODO: Write your code here
    return (candidate)

print (triplet_sum_close_to_target([-2,0,1,2],2))

print (triplet_sum_close_to_target([-3,1,2],1))

print (triplet_sum_close_to_target([1,0,1,1],100))