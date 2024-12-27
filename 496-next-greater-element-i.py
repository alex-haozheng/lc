"""The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.
"""
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # O(nums1.length + nums2.length)
        seen = {}
        stack = [nums2[0]]
        # initiate dictionary
        for n in nums2[1:]:
            while stack and n > stack[-1]:
                seen[stack.pop()] = n
            stack.append(n)
        # use dictionary
        for i in range(len(nums1)):
            nums1[i] = seen.get(nums1[i], -1)
        return nums1
            
