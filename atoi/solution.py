from typing import *

# Problem:
# Implement atoi which converts a string to an integer.
# The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. 
# Then, starting from this character takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
# The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.
# If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
# If no valid conversion could be performed, a zero value is returned.
# Note:
#   Only the space character ' ' is considered a whitespace character.
#   Assume we are dealing with an environment that could only store integers within the 
#   32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, 231 − 1 or −231 is returned.

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
