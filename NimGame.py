#!/usr/bin/python

def main():
    sol = Solution()
    win = sol.canWinNim(4)
    print win
    
class Solution(object):
    def canWinNim(self, n):  
       return False if n%4 == 0 else True

if __name__ == "__main__":
    main()