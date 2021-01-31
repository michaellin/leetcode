from typing import *

# Problem:
# Write an efficient algorithm that searches for a target value in an m x n integer matrix. The matrix has the following properties:
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        colStart = 0
        colEnd = len(matrix[0])
        rowStart = 0
        rowEnd = len(matrix)

        return self.searchMatrixRecursive(matrix, target, colStart, colEnd, rowStart, rowEnd, set())

    def searchMatrixRecursive(self, matrix, target, colStart, colEnd, rowStart, rowEnd, visited):
        if not ((rowStart <= rowEnd) and (colStart <= colEnd)):
            return False

        colCoord = (colStart + colEnd)//2
        rowCoord = (rowStart + rowEnd)//2
        if ((rowCoord, colCoord) in visited):
            return False
        visited.add((rowCoord, colCoord))
        currVal = matrix[rowCoord][colCoord]
        if (currVal == target):
            return True

        if (currVal < target):
            o1, o2 = False, False
            if (colCoord+1) < len(matrix[0]):
              o1 = self.searchMatrixRecursive(matrix, target, colCoord+1, colEnd, rowStart, rowEnd, visited)
            if (rowCoord+1) < len(matrix):
              o2 = self.searchMatrixRecursive(matrix, target, colStart, colEnd, rowCoord+1, rowEnd, visited)
            return o1 or o2
        else:
            o1, o2 = False, False
            if (colCoord-1) >= 0:
              o1 = self.searchMatrixRecursive(matrix, target, colStart, colCoord-1, rowStart, rowEnd, visited)
            if (rowCoord-1) >= 0:
              o2 = self.searchMatrixRecursive(matrix, target, colStart, colEnd, rowStart, rowCoord-1, visited)
            return o1 or o2
                      

s = Solution()
print(s.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 22))
print(s.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 15))
print(s.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 1))
print(s.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 4))
print(s.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 7))
print(s.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 11))
print(s.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 12))
print(s.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 9))
