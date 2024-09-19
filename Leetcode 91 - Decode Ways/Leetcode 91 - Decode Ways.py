# https://leetcode.com/problems/decode-ways

class Solution:

    def helper(self, s: str, idx: int) -> int:

        if idx <= 0:
            return 1

        res = 0

        # single digit
        if s[idx] != '0':
            res = res + self.helper(s, idx-1)
        
        if s[idx-1] == '1' or (s[idx-1] == '2' and s[idx] >= '0' and s[idx] <= '6'):
            res = res + self.helper(s, idx-2)

        return res

    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        return self.helper(s, len(s) - 1)
    
# Time Complexity: O(2^n)
# Space Complexity: O(n)