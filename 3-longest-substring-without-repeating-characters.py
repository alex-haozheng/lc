"""
Given a string s, find the length of the longest 
substring without repeating characters.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:\
        # sliding window
        # runtime O(n) memspace O(n)
        l, r = 0, 0
        seen = set()
        ret = 0
        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            r += 1
            ret = max(ret, r-l)
        return ret
    
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash = set([])
        l = ret = 0
        
        for r, c in enumerate(s):
            # while the character repeats with one in our current window
            while c in hash:
                hash.discard(s[l])
                l += 1
            hash.add(c)
            ret = max(ret, r-l+1)
        return ret