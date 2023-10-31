"""
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
"""

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # work backwards in these situations
				# runtime O(n) memspace O(n) ? 
        res = []
        while columnNumber > 0:
            res.append(chr(ord('A') + (columnNumber-1)%26))
            columnNumber = (columnNumber-1)//26
        return ''.join(res[::-1])