#!/usr/bin/python
## This code is done using the linked lists


def main():
    node = ListNode(2)
    newNode = ListNode(4)
    node.addNode(newNode)
    newNode = ListNode(3)
    node.addNode(newNode)
    
    secondNode = ListNode(5)
    newNode = ListNode(6)
    secondNode.addNode(newNode)
    newNode = ListNode(4)
    secondNode.addNode(newNode)
    sol = Solution()
    result = sol.addTwoNumbers(node,secondNode)
    print result
     
class ListNode(object):
    def __init__(self, x):
        self.next = None
        self.val = x

    def addNode(self,newNode):
        curNode = self
        if curNode.next != None:
            curNode = curNode.next
        curNode.next = newNode

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        import math
        firstNode = l1
        secondNode = l2
        first = 0
        count = 0
        while firstNode.next != None:
            first += int((firstNode.val)*(math.pow(10,count)))
            count += 1
            firstNode = firstNode.next
        first += int((firstNode.val)*(math.pow(10,count)))
        second = 0
        count = 0
        while secondNode.next != None:
            second += int((secondNode.val)*(math.pow(10,count)))
            count += 1
            secondNode = secondNode.next
        second += int((secondNode.val)*(math.pow(10,count)))
        
        result = first+second
        count = 0
        if result > 0:
            resultNode = ListNode(result%10)
            result = result//10
        while result // 10:
               curNode = ListNode(result%10)
               resultNode.addNode(curNode)
               result = result // 10
        curNode = ListNode(result%10)
        resultNode.addNode(curNode)  
        return resultNode
        
if __name__ == "__main__": 
    main()