'''
Design a class to calculate the median of a number stream. The class should have the following two methods:

insertNum(int num): stores the number in the class
findMedian(): returns the median of all numbers inserted in the class
If the count of numbers inserted in the class is even, the median will be the average of the middle two numbers.
'''
from random import randint

class Node:
    def __init__(self,num=None):
        self.val=num
        self.next = None

class MedianOfAStream:

    def __init__(self):
        self.root = Node()
        self.length = 0

    def print_stream(self):
        node = self.root
        if node is None:
            return
        while node:
            print(node.val,end=" ")
            node = node.next
        print()
        return

    def insert_num(self, num):
        if self.root.val is None:
            self.root.val = num
            self.length+=1
            return
        node = self.root
        if node.val <= num:
            new_node = Node(num)
            new_node.next = node
            self.root = new_node
            self.length+=1
            return
        previous = node    
        while node and node.val > num:
            node,previous = node.next, node
        new_node=Node(num)
        previous.next,new_node.next = new_node,node
        self.length+=1
        return    
            
    def find_median(self):
        #self.print_stream()
        if self.length % 2 == 1:
            node = self.root
            for _ in range(self.length//2):
                node = node.next
            return(node.val)
        else:
            node = self.root
            for _ in range(self.length//2 -1) :
                node = node.next
            next_node = node.next
            return((node.val + next_node.val)/2)

def main():
    medianOfAStream = MedianOfAStream()
    medianOfAStream.insert_num(3)
    medianOfAStream.insert_num(1)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(5)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(4)
    print("The median is: " + str(medianOfAStream.find_median()))

    for _ in range(10000):
        medianOfAStream.insert_num(randint(0,100))
        print("The median is: " + str(medianOfAStream.find_median()))


main()
