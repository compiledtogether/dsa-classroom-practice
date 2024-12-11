# https://leetcode.com/problems/fibonacci-number

class Solution:
    def fib(self, n: int) -> int:
        # if n<=1:
        #     return n

        # return self.fib(n-1) + self.fib(n-2)
        
# Time complexity: O(2^n)
# Space complexity: O(n)
    
        a,b = 0,1

        if n<=1:
            return 1

        for i in range(2, n+1):
            a,b = b, a+b

        return b
    
# Time Complexity: O(n)
# Space Complexity: O(1)
        