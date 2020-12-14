from typing import *
# Problem:
# Given an absolute path for a file (Unix-style), simplify it. Or in other words, convert it to the canonical path.
# In a UNIX-style file system, a period '.' refers to the current directory. Furthermore, a double period '..' moves the directory up a level.
# Note that the returned canonical path must always begin with a slash '/', and there must be only a single slash '/' between two directory names. 
# The last directory name (if it exists) must not end with a trailing '/'. Also, the canonical path must be the shortest string representing the absolute path.

class Solution:
    def simplifyPath(self, path: str) -> str:
        # split the paths by /
        paths = [x for x in path.split('/') if x != '']
        queue = []
        for d in paths:
          if (d == '..'):
            if len(queue) != 0:
              queue.pop(-1)
          elif (d != '.'):
            queue.append(d)

        # construct the path
        path = '/'
        for d in queue:
          path += d
          path += '/'

        return path[:-1] if len(path) > 1 else path
s = Solution()
print(s.simplifyPath("/home//foo/"))
print(s.simplifyPath("/a/./b/../../c/"))
print(s.simplifyPath("../"))

