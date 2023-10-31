"""
Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].

For example, swapping at indices 0 and 2 in "abcd" results in "cbad".
"""
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal): return False
        if s == goal and len(set(s)) < len(s): return True # is there exists extra of oen letter
        dif = [(a,b) for a, b in zip(s, goal) if a != b]
        return len(dif) == 2 and dif[0] == dif[1][::-1]