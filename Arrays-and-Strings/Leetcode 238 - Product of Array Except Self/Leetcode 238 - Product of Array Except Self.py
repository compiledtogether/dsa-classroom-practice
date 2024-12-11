# https://leetcode.com/problems/product-of-array-except-self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        output = [1] * nums_len

        # # Using DP without space optimization    
        # prefix = [1] * nums_len
        # suffix = [1] * nums_len
        # for i in range(1, nums_len):
        #     prefix[i] = prefix[i-1] * nums[i-1]
        #     suffix[nums_len - i - 1] = suffix[nums_len - i] * nums[nums_len - i]
            
        # for i in range(nums_len):
        #     output[i] = prefix[i] * suffix[i]

        # Using DP with space optimization    
        prefix_product = 1    
        for i in range(nums_len):
            output[i] = prefix_product
            prefix_product *= nums[i]
            
        sufffix_product = 1
        for i in range(nums_len-1,-1,-1):
            output[i] *= sufffix_product
            sufffix_product *= nums[i]
        
        return output
    
# Time complexity: O(n)
# Space complexity: O(1)