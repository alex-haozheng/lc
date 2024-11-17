'''
Given n pairs of parentheses, write a function to 
generate all combinations of well-formed parentheses.
'''

# generate all combinations with a stack with recursion like iterations
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # time O(?) space O(?)
        st = [(0,0,'')]
        ret = []
        
        while st:
            (l, r, s) = st.pop()
            
            if l+r == 2*n:
                ret.append(s)
            else:
                if l < n:
                    st.append((l+1, r, s+'('))
                if r < l:
                    st.append((l, r+1, s+')'))

        return ret