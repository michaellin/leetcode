from typing import *

class Solution:
    def isPalindrome(self, x: int) -> bool:
        digits = []
        div = 10
        if (x < 0):
            return False
        while (x // (div/10) != 0):
            digits.append(int((x%div)/(div/10)))
            div *= 10
        
        idxInit = 0
        idxEnd = len(digits)-1
        while (idxInit <= idxEnd):
            if (digits[idxInit] != digits[idxEnd]):
                return False
            idxInit += 1
            idxEnd -= 1
            
        return True

s = Solution()
print(s.isPalindrome(101))
print(s.isPalindrome(-101))
print(s.isPalindrome(0))
print(s.isPalindrome(1040))
