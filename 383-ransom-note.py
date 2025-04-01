"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # O(n) memspace O(m+n) runtime
        count = {}
        for c in magazine:
            count[c] = count.get(c, 0) + 1
        for c in ransomNote:
            if c in count and count[c] > 0:
                count[c] -= 1
            else:
                return False
        return True
    
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # O(m+n) memspace O(m+n) runtime
        r = sorted(ransomNote)
        m = sorted(magazine)
        i, j = 0, 0
        while i < len(r) and j < len(m):
            if r[i] < m[j]:
                return False
            elif r[i] == m[j]:
                i += 1
            j += 1
        return i == len(r)
