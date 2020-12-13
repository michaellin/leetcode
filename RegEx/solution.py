from typing import *

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # get pattern number or characters without wildcard
        charsNum = 0
        pIdx = 0
        while (pIdx < len(p)):
          if (pIdx + 1 < len(p)) and p[pIdx + 1] == '*':
            pIdx += 2
          else:
            charsNum += 1
            pIdx += 1
        return self.isMatchRecursive(s, p, charsNum)

    def isMatchRecursive(self, s: str, p: str, pCharsLeft: int) -> bool:
      if ((len(s) == 0) and (len(p) == 0)):
        return True
      if (len(p) > 1) and p[1] == '*':
        # recurve deep first if we have enough pattern chars left
        output = False
        if ((len(s) > pCharsLeft) and (p[0] in {s[0], '.'})):
          return self.isMatchRecursive(s[1:], p, pCharsLeft) or \
                 self.isMatchRecursive(s, p[2:], pCharsLeft)      # backtrack
        elif (len(s) == 0) and (pCharsLeft == 0):
          return True
        else:
          # try to match the rest
          return self.isMatchRecursive(s, p[2:], pCharsLeft)

      if (len(s) == 0) != (len(p) == 0):
        return False
      if (p[0] in {s[0], '.'}):
        return self.isMatchRecursive(s[1:], p[1:], pCharsLeft-1)
      return False

s = Solution()
assert s.isMatch("aa","a") == False
assert s.isMatch("","") == True
assert s.isMatch("aa","a*") == True
assert s.isMatch("a","c*a") == True
assert s.isMatch("asdfgksfk",".*f") == False
assert s.isMatch("aaa","a*aaaa") == False
assert s.isMatch("aaa","a*aaa") == True
assert s.isMatch("aaabbbbb","a*aaab*bbbbb") == True
assert s.isMatch("abc",".*d") == False
assert s.isMatch("abd",".*d") == True
assert s.isMatch("a","a*") == True
assert s.isMatch("",".*") == True
assert s.isMatch("a","") == False
assert s.isMatch("","a") == False
assert s.isMatch("aasdfasdfasdfasdfas","aasdf.*asdf.*asdf.*asdf.*s") == True
print("All test passed")
