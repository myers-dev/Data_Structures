class Pair:
  def __init__(self, first, second):
    self.first = first
    self.second = second
  def __str__(self):
    return(str(self.first)+","+str(self.second))
  def __repr__(self):
    return("["+str(self.first)+","+str(self.second)+"]")

def merge_intervals(v):
    r=[]
    for p in v:
        #print(r)
        if len(r)==0:
            r.append(p)
        else:
            if p.first > r[-1].second:
                r.append(p)
            else:
                r[-1].second=p.second
    return (r)

v=[Pair(1,5),Pair(3,7),Pair(4,6),Pair(6,8)]
print(merge_intervals(v))

v=[Pair(10,12),Pair(12,15)]
print(merge_intervals(v))
