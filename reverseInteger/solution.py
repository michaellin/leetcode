from typing import *

# Problem:
# Given a 32-bit signed integer, reverse digits of an integer.
# Note:
#   Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
#   For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

class Solution:
    def reverse(self, x: int) -> int:
        div = 10
        digits = []
        sign = 1
        if (x < 0):
            sign = -1
            x = -x
        while x // (div/10) != 0:
            digits.append((x % div)//(div/10))
            div *= 10
        mag = 0
        for d in digits:
          mag += d*(div/100)
          div /= 10
        res = sign*int(mag)
        if (res != min(max(res, -2**31), 2**31-1)):
            return 0
        return res

s = Solution()
print(s.reverse(100))
print(s.reverse(-123))
print(s.reverse(120))
print(s.reverse(0))
