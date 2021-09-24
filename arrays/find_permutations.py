def find_permutations(nums):
    debug = False
    result = []
  
    result.append([nums.pop()])

    while nums:
        n = nums.pop()
        if debug :
            print(f"n={n} nums={nums} result={result}")
        new_result=[]
        l=len(result[0])
        for position in range(l+1):
            for element in result:
                if debug:
                    print(f"p= {element[0:position]} + {[n]} + {element[0:l]}")
                p = element[0:position] + [n] + element[position:l]
                if debug:
                    print(f"position={position} n={n} element={element} p={p}")
                new_result.append(p)
        result = new_result
        if debug:
            print(f"=====result={result}")
    return (result)


def main():
  print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))


main()