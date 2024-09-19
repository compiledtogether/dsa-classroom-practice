# https://leetcode.com/problems/climbing-stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        # if n<=1:
        #     return 1
        
        # return self.climbStairs(n-1) + self.climbStairs(n-2)
        
# Time complexity: O(2^n)
# Space complexity: O(n)

        a,b = 1,1

        if n<=1:
            return 1

        for i in range(2, n+1):
            a,b = b, a+b

        return b

# Time Complexity: O(n)
# Space Complexity: O(1)