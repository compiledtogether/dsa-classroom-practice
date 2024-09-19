# https://leetcode.com/problems/n-th-tribonacci-number

class Solution:
    def tribonacci(self, n: int) -> int:
        # if n == 0:
        #     return n
        # if n <= 2:
        #     return 1

        # return self.fib(n-1) + self.fib(n-2) + elf.fib(n-3)
        
# Time complexity: O(3^n)
# Space complexity: O(n)
        
        zero,one,two = 0,1,1
        if n==0:
            return zero
        if n<3:
            return one

        for i in range(3,n+1):
            curr = zero+one+two
            zero,one,two = one,two,curr

        return two

# Time complexity: O(n)
# Space complexity: O(1)