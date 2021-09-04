def max_sub_array_of_size_k(k, arr):
  m=sum(arr[0:k])
  csum=m
  for i in range(0,len(arr)-k):
      csum=csum-arr[i]+arr[k+i]
      if csum>m:
          m=csum
  return (m)

a=[2, 1, 5, 1, 3, 2]
k=3

print(max_sub_array_of_size_k(k,a))

a=[2, 3, 4, 1, 5]
k=2

print(max_sub_array_of_size_k(k,a))