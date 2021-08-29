import time

def find_least_common_number(a, b, c):
    i1,i2,i3=0,0,0
    while not (a[i1]==b[i2]==c[i3]) and ( i1<len(a) and i2<len(b) and i3<len(c)):
        #print(i1,i2,i3,a[i1],b[i2],c[i3])
        time.sleep(1)
        
        if a[i1]>=b[i2] and a[i1]>=c[i3]:
            #print("-1-")
            i2t=i2+1 if a[i1]>b[i2] else i2
            i3t=i3+1 if a[i1]>c[i3] else i3
            i2,i3=i2t,i3t
        elif b[i2]>=a[i1] and b[i2]>=c[i3]:
            #print("-2-")
            i1t=i1+1 if b[i2]>a[i1] else i1
            i3t=i3+1 if b[i2]>c[i3] else i3
            i1,i3=i1t,i3t
        elif c[i3]>=a[i1] and c[i3]>=b[i2]:
            #print("-3-")
            i1t=i1+1 if c[i3]>a[i1] else i1
            i2t=i2+1 if c[i3]>b[i2] else i2 
            i1,i2=i1t,i2t
        if i1>len(a)-1:
            i1-=1
        if i2>len(b)-1:
            i2-=1
        if i3>len(c)-1:
            i3-=1
    if (a[i1]==b[i2]==c[i3]):
        return (a[i1])
    return (-1)


a=[6,7,10,25,30,63,64]
b=[0,4,5,6,7,8,50]
c=[1,6,10,14]

print (find_least_common_number(a,b,c))

