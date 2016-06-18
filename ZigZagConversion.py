#!/usr/bin/python

def main():
    sol = Solution()
    sol.convert('PAYPALISHIRING',3)

class Solution(object):
    def convert(self, s, numRows):
        #Creatr a list that you can add the string for each row to 
        rowStringList= []
        testDone = False
        print numRows
        for a in range(numRows):
            print a
            rowStringList.append('')
           
        for i in range(numRows):
            print i
            rowStringList[(i%numRows)] += (s[i])
        for i in range(numRows,-1):
            rowStringList[(i%numRows)] += (s[i])
        
        print rowStringList            
        
if __name__ == '__main__':
    main()