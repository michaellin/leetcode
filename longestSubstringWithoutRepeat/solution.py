from typing import *

# Problem:
# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # we could do a brute force recursive search were 
        # function is called without first char and another
        # call without last char and take the max of that.
        # But this is quadratic for memory and runtime.
        
        # how to search
        # determine if good substring
        #   this can be hashset
        # "pw[ewk]ew"
        
        # search from beginning and end
        ci_l = 0
        ci_r = 0
        cf_l = len(s) - 1
        cf_r = len(s) - 1
        
        # keep track of the longest substring
        longest_ss = 0
        # curr_longest_i = 0
        # curr_longest_f = 0
        chars_sofar_i = set()
        chars_sofar_f = set()
        
        # create a hashset for tracking repeats
        while cf_r >= ci_l:
            
            while (ci_r <= cf_r and s[ci_r] not in chars_sofar_i):
                chars_sofar_i.add(s[ci_r])
                ci_r += 1
            
            while (cf_l >= ci_l and s[cf_l] not in chars_sofar_f):
                chars_sofar_f.add(s[cf_l])
                cf_l -= 1
            
            # advance whichever is shorter
            curr_longest_i = ci_r - ci_l
            curr_longest_f = cf_r - cf_l
            if (curr_longest_i < curr_longest_f):
                # save the longest
                longest_ss = max(longest_ss, curr_longest_f)
                # shrink the initial chunk 
                chars_sofar_i.discard(s[ci_l])
                ci_l += 1
            else:
                # save the longest
                longest_ss = max(longest_ss, curr_longest_i)
                # shrink final chunk
                chars_sofar_f.discard(s[cf_r])
                cf_r -= 1
                
        return longest_ss

s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("pwwkew"))
print(s.lengthOfLongestSubstring(""))
