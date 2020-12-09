from typing import *
# question:
# you have a company where each employee has an EID: integer and CRC: integer,
# The CRC is calculated by the number of employees that report to a certain employee
# lets say that we can keep track of employee reporting with a map
# { 10: [20, 30],
#   20: [40, 50],
#   30: [],
#   40: [],
#   50:[]
# }
# make a function that calcualtes the CRC for a speific EID.
# Also, if this function is called multiple times, how could you speed up the process.

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.visited = set()
        self.floodFillRecursive(image, sr, sc, oldColor=image[sr][sc], newColor=newColor)
        return image


    def floodFillRecursive(self, image, sr, sc, oldColor, newColor):
        if (image[sr][sc] != oldColor):
            return None
        self.visited.add((sr,sc))
        if (image[sr][sc] == oldColor):
          image[sr][sc] = newColor
        if (sr < len(image) - 1 and (sr+1, sc) not in self.visited):
          self.floodFillRecursive(image, sr+1, sc, oldColor, newColor)
        if (sr > 0) and (sr-1, sc) not in self.visited:
          self.floodFillRecursive(image, sr-1, sc, oldColor, newColor)
        if (sc < len(image[0]) - 1) and (sr, sc+1) not in self.visited:
          self.floodFillRecursive(image, sr, sc+1, oldColor, newColor)
        if (sc > 0) and (sr, sc-1) not in self.visited:
          self.floodFillRecursive(image, sr, sc-1, oldColor, newColor)
        return None

        
s = Solution()
print(s.floodFill([[1,2],[3,1]], 0, 0, 5))
print(s.floodFill([[1]], 0, 0, 4))
