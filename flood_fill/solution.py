from typing import *

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
