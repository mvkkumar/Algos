#1/usr/bin/python

def main():
    sol = Solution()
    isPal = sol.isPalindrome(10001)
    print isPal

class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        # First Convert the number to Postive and change that to String
        stringNum = str(x)
        for charNum in range(len(stringNum)/2):
            if stringNum[charNum] != stringNum[-1-charNum]:
                return False
            else:
                continue
        return True 
                 
        

if __name__ == "__main__":
    main()