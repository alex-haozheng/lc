"""
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.
"""

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # string matching logic
        # basicaly with s we already have an x amount of repeats 
        # the first char and the last char should represent the first and last char of the substring
        # if it was to be repeatable 
        # thus if we repeat a string as such we should ahve the original string composed in the midst of 2*s
        return s in (2 * s)[1:-1]