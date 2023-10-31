"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ret = 0
        i, j = 0, 1
        counter = {s[0]: 1}
        while j < len(s):
            counter[s[j]] = counter.get(s[j], 0) + 1
            m_count = max(counter.values())
            if (j-i+1) - m_count <= k:
                print(j, i, m_count)
                ret = max(ret, j-i+1)
            else:
                counter[s[i]] -= 1
                i += 1
            j += 1
                
        return ret