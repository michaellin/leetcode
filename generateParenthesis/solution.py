from typing import *

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parenCombs = []
        self.generateParenRecursive(n, parenOpen=0, strSofar="", out=parenCombs)
        return parenCombs
    
    def generateParenRecursive(self, n, parenOpen, strSofar, out):
        if (n == 0) and (parenOpen == 0):
            out.append(strSofar)
            return
        if (parenOpen > 0):
            # we can either open or close
            # open
            if (n > 0):
              self.generateParenRecursive(n - 1, parenOpen + 1, strSofar + "(", out)
            #close
            self.generateParenRecursive(n, parenOpen - 1, strSofar + ")", out)
        else:
            # we can only open
            self.generateParenRecursive(n - 1, parenOpen + 1, strSofar + "(", out)

s = Solution()
print(s.generateParenthesis(0))
print(s.generateParenthesis(1))
print(s.generateParenthesis(2))
