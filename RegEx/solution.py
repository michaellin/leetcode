from typing import *

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sIdx = 0
        pIdx = 0
        while sIdx != len(s) and pIdx != len(p):
          # get pattern first
          pat = p[pIdx]
          pIdx += 1
          # find decorator first
          if (pIdx < len(p)) and p[pIdx] == '*':
            pIdx += 1
            repIdx = pIdx
            repCount = 0
            repPat = pat
            # check for repeats in pattern
            print(repPat)
            while repIdx < len(p) and ((p[repIdx] == repPat) or (pat == '.')):
              repIdx += 1
              repCount += 1
            pIdx += repCount
            while sIdx < len(s) and ((s[sIdx] == pat) or pat == '.'):
              sIdx += 1
              if (repCount > 0):
                repCount -= 1
            if (repCount != 0):
              return False
          else:
            if (s[sIdx] != pat and pat != '.'):
              return False
            sIdx += 1
          
        return sIdx == len(s) and pIdx == len(p)

s = Solution()
print(s.isMatch("aa","a"))
print(s.isMatch("",""))
print(s.isMatch("aa","a*"))
print(s.isMatch("a","c*a"))
print(s.isMatch("a","c*a"))
print(s.isMatch("asdfgksfk",".*f"))
print(s.isMatch("aaa","a*aaaa"))
print(s.isMatch("aaa","a*aaa"))
print(s.isMatch("aaabbbbb","a*aaab*bbbbb"))
print(s.isMatch("abc",".*d"))
