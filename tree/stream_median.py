from random import randrange
import math

stream = []
for i in range(10):
    r = randrange(10)
    stream.append(r)
    sorted_stream=sorted(stream)
    if i<2:
        continue
    if len(stream)%2 == 1:
        print(r,stream,sorted_stream,sorted_stream[len(stream)//2])
    else:
        a=sorted_stream[len(stream)//2-1]
        b=sorted_stream[len(stream)//2]
        print(r,sorted_stream,(a+b)/2 ,a,b)