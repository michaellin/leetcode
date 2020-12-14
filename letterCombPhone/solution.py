from typing import *

# Problem:
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

class Solution:
    digitMap = {
      '2': "abc",
      '3': "def",
      '4': "ghi",
      '5': "jkl",
      '6': "mno",
      '7': "pqrs",
      '8': "tuv",
      '9': "wxyz"
    }
    def letterCombinations(self, digits: str) -> List[str]:
        if (len(digits) == 0):
          return []
        if (len(digits) == 1):
          return [l for l in self.digitMap[digits[0]]]
        output = self.combine(self.digitMap[digits[0]], self.digitMap[digits[1]])
        i = 2
        while i < len(digits):
          output = self.combine(output, self.digitMap[digits[i]])
          i += 1
        return output

    def combine(self, list1, list2):
        out = []
        for i in list1:
          for j in list2:
            out.append(i + j)
        return out

s = Solution()
print(s.letterCombinations(""))
print(s.letterCombinations("3"))
print(s.letterCombinations("239"))
