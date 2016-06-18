#!/usr/bin/python

class Solution(object):
    
    def lengthOfLongestSubstring(self, s):
        maxLength,curLength = 0,0
        longSubString = ''
        testDone = False
        #curSubString = s[0] if len(s) > 0 else ''
        
        (curSubString,c) = self.lengthOfSubstring(s,'')
        if len(longSubString)< len(curSubString): longSubString = curSubString
        while (testDone == False):
            if c is not '':
                s = s[s.index(c)+1:]
                (curSubString,c) = self.lengthOfSubstring(s,c)
                if len(longSubString)< len(curSubString): longSubString = curSubString
            elif c is '':
                testDone = True
                break
        if len(longSubString)< len(curSubString): longSubString = curSubString    
        return len(longSubString)
        
    def lengthOfSubstring(self,s,c):
        length = 0
        curSubString = ''
        # This is called recursively from the main function to come up with the length of the substrng #
        if c is '':
            for a in range(len(s)):
                if s[a] not in curSubString:
                    curSubString +=s[a]
                elif s[a] in curSubString:
                    return (curSubString,s[a])
        elif c is not '':
            curSubString += s[:s.index(c)+1]
            for a in range(s.index(c)+1,len(s)):
                if s[a] not in curSubString:
                    curSubString +=s[a]
                elif s[a] in curSubString:
                    return (curSubString,s[a])
        return (curSubString,'')
        
def main():
    sol = Solution()
    length = sol.lengthOfLongestSubstring("dvdf")
    print length
    return
      
if __name__ == "__main__":
    main()