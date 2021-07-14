class heap:
    def __init__(self,h):
        self.h = h
        self.max = len(h) - 1

    def get_parent(self,idx):
        if idx == 0:
            parent = None
        else:
            parent = (idx - 1)//2
        return(parent)

    def get_children(self,idx):
        children1 = idx * 2 + 1
        children2 = idx * 2 + 2

        if children1 > self.max:
            children1 = None
        if children2 > self.max:
            children2 = None
        return ((children1,children2))
    
    def bubbledown(self,start):
        # changing the logic ; bubble down the top until no changes will be made
        swap = True
        idx = start
        while swap:
            swap = False
            children1,children2 = self.get_children(idx)
            #print(idx,'->',children1,children2)
            # both is None
            if children1 is None and children2 is None:
                pass
            # children2 is None
            elif children2 is None and children1 is not None:
                if self.h[children1] < self.h[idx]:
                    # swap time !
                    self.h[children1],self.h[idx] = self.h[idx],self.h[children1]
                    idx = children1
                    swap = True
            else:
                mchildren=min(children1,children2,key=lambda x: self.h[x])
                #print('mchildren=',mchildren)
                if self.h[mchildren] < self.h[idx]:
                    # swap time !
                    self.h[mchildren],self.h[idx] = self.h[idx],self.h[mchildren]
                    idx = mchildren
                    swap = True

        return 

    def convertMax(self):
        for i in range(self.max,-1,-1):
            self.bubbledown(i)

def convertMax(maxHeap):
    h = heap(maxHeap)
    h.convertMax()
    print(h.h)
    
