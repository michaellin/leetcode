from typing import *

class Solution:
  def myAtoi(self, s: str) -> int:
    if s == '' or len(s) > 200:
      return 0

    # str_res = ""
    stringSize = len(s)
    startIdx = 0

    # find the index at which non-white space starts
    i = 0
    while (s[i] == ' '):
      i += 1
      if (i == stringSize): return 0

    sign = 1
    if (s[i] in ['+', '-']):
      if s[i] == '-': sign = -1
      i+= 1
    startIdx = i
    while (i < stringSize and s[i].isnumeric()):
      i += 1
    if (startIdx == i):
      return 0
    return max(min(sign*int(s[startIdx:i]), 2**31-1), -2**31)
        
s = Solution()
print(s.myAtoi("           -42"))
print(s.myAtoi("4193 with words"))
print(s.myAtoi("words and 981"))
print(s.myAtoi("-91283472332"))
