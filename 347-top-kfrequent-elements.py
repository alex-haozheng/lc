"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
"""

class Solution:
    # O(n) memspace O(n) runtime
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        def getValue(e):
            return e[1]
        for e in nums:
            if e in hash:
                hash[e] += 1
            else:
                hash[e] = 1
        return [i[0] for i in sorted(hash.items(), key=getValue)][-k:]
        