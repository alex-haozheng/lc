"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # O(n) memspace O(n) runtime
        h1 = {}
        h2 = {}
        for c1, c2 in zip(s, t):
            h1[c1] = h1.setdefault(c1, 0) + 1
            h2[c2] = h2.setdefault(c2, 0) + 1
        return h1 == h2 and len(s) == len(t)
            
    def isAnagram(self, s: str, t: str) -> bool:
        # O(1) memspace O(logn) runtime
        return sorted(s) == sorted(t)