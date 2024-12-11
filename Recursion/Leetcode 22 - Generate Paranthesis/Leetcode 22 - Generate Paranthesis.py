# https://leetcode.com/problems/generate-parentheses

class Solution:
    def helper(self, n, o, c, curr, res) -> List[str]:
        # base condition
        # if c == n:
        if len(curr) == 2*n:
            res.append(curr)
            return
        # pick open paranthesis
        if o < n:
            self.helper(o+1, c, curr + '(')
        # pick close paranthesis
        if o > c:
            self.helper(o, c+1, curr + ')')
            
    def generateParenthesis(self, n: int) -> List[str]:
        res: List[str] = []
        self.helper(n, 0, 0, "", res)
        return res
        
        
# Time Complexity: O(4^n/sqrt(n))
# Space Complexity: O(4^n/sqrt(n))