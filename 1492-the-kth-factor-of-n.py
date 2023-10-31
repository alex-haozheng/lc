"""
You are given two positive integers n and k. A factor of an integer n is defined as an integer i where n % i == 0.

Consider a list of all factors of n sorted in ascending order, return the kth factor in this list or return -1 if n has less than k factors.
"""
# O(sqrt(n)) runtime O(1) space
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        # loop through possible first half of factors
        for f in range(1, int(n**0.5)+1):
            if n % f == 0:
                k -= 1
                if k == 0: return f
        # same loop but we find inverse pair factor
        for f in range(int(n**0.5), 0, -1):
            # double count acutal squares
            if f*f == n: continue
            if n % f == 0:
                k -= 1
                if k == 0: return n // f
        return -1