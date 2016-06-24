#!/usr/bin/python

def main():
    sol = Solution()
    ret = sol.isMatch("aaa","ab*a*c*a")
    print ret
# 
# class Solution(object):
#     def isMatch(self, s, p):
#         # s and p both are Strings, p can also be . or * 
#         #. means one instance of any single Char
#         # * means 0 or more occurances of the previous charcater   
#         repChar = ''
#         rep = False
#         for charIndex in range(len(s)):
#             if (charIndex+1 > len(p)) and (rep == False ):
#                 return False
#             if ( rep == False ) and ( p[charIndex] == '.' ):
#                 rep = False
#                 continue
#             elif ( rep == False ) and ( p[charIndex] == '*' ): 
#                 rep = True
#                 if charIndex > 0:
#                     repChar = p[charIndex - 1]
#                     if (repChar == s[charIndex]) or repChar == '.':
#                         continue
#                     else:
#                         return False
#                 else:
#                     return False     
#             else:
#                 
#                 if (rep == True and ( repChar == s[charIndex] or repChar == '.')):
#                     continue
#                 elif p[charIndex] == s[charIndex]:
#                     rep = False
#                     continue
#         return True
    
class Solution(object):
    def isMatch(self, s, p):
        repChar = False
        pCharIndex = -1
        sCharIndex = -1
        testDone = False
        sEnded, pEnded = False, False
        while testDone == False:
            if sCharIndex+len(s) < 0:
                sEnded = True
            if pCharIndex+len(p) <0:
                pEnded =True
            if pEnded and sEnded :
                testDone = True
                break
            elif pEnded and (sEnded == False ):
                return False
            elif sEnded and (pEnded == False ):
                if (repChar and (pCharIndex+len(p)==0)):
                    testDone = True
                    break
                elif p[pCharIndex] == '*':
                    pCharIndex -= 2
                    continue
                else:
                    return False
            if p[pCharIndex] == '*':
                repChar = True
                pCharIndex -= 1
            else:
                if repChar == True:
                    if p[pCharIndex] == s[sCharIndex] or p[pCharIndex] == '.':
                        while (sCharIndex+len(s) > 0) and ( s[sCharIndex] == s[sCharIndex-1]) :
                            sCharIndex -= 1
                        while (pCharIndex+len(p) > 0) and (p[pCharIndex] == p[pCharIndex-1] or p[pCharIndex] == '.'):
                            pCharIndex -= 1
                        #if (sCharIndex+len(s)>=0):sCharIndex -= 1
                        #if (pCharIndex+len(p)>0):
                        #    pCharIndex -= 1
                        repChar = False
                        if p[pCharIndex] == '.': 
                            sCharIndex -= 1
                            repChar = True
                    else:
                        pCharIndex -= 1
                        repChar = False
                elif repChar == False:
                        if p[pCharIndex] == s[sCharIndex] or p[pCharIndex] == '.':
                            if (pCharIndex+len(p)>=0): pCharIndex -=1 
                            sCharIndex -= 1
                        else:
                            return False
            
        return True
    
if __name__ == "__main__":
    main()