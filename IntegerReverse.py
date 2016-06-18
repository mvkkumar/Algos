#!usr/bin/python/

def main():
    sol = Solution()
    sol.reverse(10)



class Solution(object):
    def reverse(self, x):
        import math
        count = 0
        nums = []
        result = 0
        negative = False
        if x < 0: negative = True
        while ((abs( x) % 10 ) >= 0) and (abs(x)/1 != 0 ) :
            nums.append(abs(x)%10)
            x = abs(x) // 10
        for x in range(len(nums)):
            result += int(nums[x]*math.pow(10,(len(nums)-x-1)))
        if result > 2147483647: result = 0
        if negative == True: result = result * -1
        return result
            
            
if __name__ == "__main__":
    main()