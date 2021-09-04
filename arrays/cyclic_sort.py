from time import sleep

def cyclic_sort(nums):
    swap=True
    n=0
    while swap:
        swap=False
        for i in range(len(nums)):
            #print(nums)
            #print(f"nums[{i}]={nums[i]}")
            #sleep(1)
            if nums[i]!=i+1:
                #print("swap!")
                nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]
                swap=True
        n+=1
    #print(f"{n} times we went through the array")
    return(nums)
                


a=[3, 1, 5, 4, 2]
print(cyclic_sort(a))

a=[2, 6, 4, 3, 1, 5]
print(cyclic_sort(a))

a=[1, 5, 6, 4, 3, 2]
print(cyclic_sort(a))