from typing import *

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
          return s
        ptrLeft1 = 0
        ptrLeft2 = len(s)
        
        ptrRight1 = 0
        ptrRight2 = len(s)
        
        leftLongest, rightLongest = 0, 0
        leftLongestIdx, rightLongestIdx = 0, len(s)
        while (ptrRight2 >= leftLongestIdx and ptrLeft1 <= rightLongestIdx and ptrLeft1 != len(s) and ptrRight2 != 0):
            if (ptrLeft2 == len(s)):
                # search for longest left palindrome            
                while (ptrLeft2 >= ptrLeft1):
                    if (self.isPalindrome(s[ptrLeft1:ptrLeft2])):
                        leftLongest = ptrLeft2-ptrLeft1
                        leftLongestIdx = ptrLeft2
                        break
                    ptrLeft2 -= 1
            if (ptrRight1 == 0):
                # search for the longest right palindrome
                while (ptrRight2 >= ptrRight1):
                    if (self.isPalindrome(s[ptrRight1:ptrRight2])):
                        rightLongest = ptrRight2-ptrRight1
                        rightLongestIdx = ptrRight1
                        break
                    ptrRight1 += 1
            if (leftLongest > rightLongest):
                ptrRight2 -= 1
                ptrRight1 = 0
                rightLongest = 0
            else:
                ptrLeft1 += 1
                ptrLeft2 = len(s)
                leftLongest = 0
        if (leftLongest > rightLongest):
            return s[ptrLeft1:ptrLeft2]
        else:
            return s[ptrRight1:ptrRight2]
        
        
    def isPalindrome(self, s):
        si = 0
        sf = len(s) - 1
        while (sf >= si):
            if ((sf == si or (sf-si)==1) and s[sf] == s[si]):
                return True
            if (s[sf] == s[si]):
                si += 1
                sf -= 1
            else:
              return False
        return False

s = Solution()
print(s.isPalindrome("bb"))
print(s.isPalindrome("bab"))
print(s.isPalindrome("aa"))
print(s.isPalindrome("ba"))

print("answer {0}".format(s.longestPalindrome("babad")))
print("answer {0}".format(s.longestPalindrome("cbbd")))
print("answer {0}".format(s.longestPalindrome("a")))
print("answer {0}".format(s.longestPalindrome("ac")))
print("answer {0}".format(s.longestPalindrome("bb")))
print("answer {0}".format(s.longestPalindrome("cbbd")))
print("answer {0}".format(s.longestPalindrome("cbbdalancbbd")))
print("answer {0}".format(s.longestPalindrome("nalan")))
print("answer {0}".format(s.longestPalindrome("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")))
