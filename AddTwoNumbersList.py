#!/usr/bin/python
#Adding two numbers when the lists are given
def main():
    l1 = [2,4,3,1]
    l2 = [5,6,4,5]
    sol = Solution()
    sol.addTwoNumbers(l1,l2)
    
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        resultList = []
        import math
        count = 0
        first,second = 0,0
        a = len(l1)
        for a in range(len(l1)):
            first += (l1[a]*(math.pow(10,count)))
            count += 1
        count = 0
        for a in range(len(l2)):
            second += (l2[a]*(math.pow(10,count)))
            count += 1
        result = int(first+second)
        while result // 10: 
               resultList.append(result%10)
               result = result // 10
        resultList.append(result%10)
        print resultList
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
if __name__ == "__main__":
    main()