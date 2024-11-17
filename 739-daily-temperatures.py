'''
Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number of days you have to 
wait after the ith day to get a warmer temperature. If there is no future day
for which this is possible, keep answer[i] == 0 instead.
'''

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        ret = [0 for _ in temperatures]

        for i, t in enumerate(temperatures):
            while st and st[-1][1] < t:
                j, _ = st.pop()
                ret[j] = i-j
            st.append((i, t))
        return ret