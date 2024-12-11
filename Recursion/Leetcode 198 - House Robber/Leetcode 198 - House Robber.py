# https://leetcode.com/problems/house-robber

class Solution:

    # # bottom up
    # def helper(self, nums: List[int], idx: int):
    #     if idx >= len(nums):
    #         return 0
    #     rob = nums[idx] + self.helper(nums, idx+2)
    #     dontrob = self.helper(nums, idx+1)
    #     return max(rob, dontrob)

    # def rob(self, nums: List[int]) -> int:
    #     return self.helper(nums, 0)   

    # # top down
    # def helper(self, nums: List[int], idx: int):
    #     if idx < 0:
    #         return 0
    #     rob = nums[idx] + self.helper(nums, idx-2)
    #     dontrob = self.helper(nums, idx-1)
    #     return max(rob, dontrob)

    # def rob(self, nums: List[int]) -> int:
    #     return self.helper(nums, len(nums) - 1)   
    
# Time Complexity: O(2^n)
# Space Complexity: O(n)

    def rob(self, nums: List[int]) -> int:
        nums.append(0)
        
        for i in range(len(nums) - 3, -1, -1):
            nums[i] = max(nums[i] + nums[i + 2], nums[i + 1])
            
        return nums[0]
    
# Time Complexity: O(n)
# Space Complexity: O(1)

    