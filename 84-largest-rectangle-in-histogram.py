"""
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.
"""

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st, res = [], 0

        for i, h in enumerate(heights):
            start = i
            while st and st[-1][1] > h:
                index, height = st.pop()
                res = max(res, height * (i-index))
                start = index # evening out the layers
            st.append((start, h))

        # left over stack
        for i, h in st:
            res = max(res, h * (len(heights) - i))
        return res