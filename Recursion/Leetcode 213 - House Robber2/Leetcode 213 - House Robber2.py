# https://leetcode.com/problems/house-robber-ii

class Solution:
    def rob(self, nums: List[int]) -> int:
        # # top down approach
        # def helper(idx: int, start: int):
        #     if start == len(nums) - 1 and idx < 1:
        #         return 0
        #     if start == len(nums) - 2 and idx < 0:
        #         return 0

        #     rob = nums[idx] + helper(idx-2, start)
        #     dontrob = helper(idx-1, start)
        #     return max(rob, dontrob)

        # if len(nums) == 1:
        #     return nums[0]

        # return max(helper(len(nums)-1, len(nums)-1), helper(len(nums)-2, len(nums)-2))
        
# Time Complexity: O(2^n)
# Space Complexity: O(n)

        # if len(nums) == 1:
        #     return nums[0]

        # secondNums = nums[1:]
        # nums[-1] = 0
        # secondNums.append(0)
        # for i in range(len(nums) - 3, -1, -1):
        #     nums[i] = max(nums[i] + nums[i+2], nums[i+1])

        # for i in range(len(secondNums) - 3, -1, -1):
        #     secondNums[i] = max(secondNums[i] + secondNums[i+2], secondNums[i+1])

        # return max(nums[0], secondNums[0])
        
# Time Complexity: O(n)
# Space Complexity: O(n)

        if len(nums) == 1:
            return nums[0]


        rob1, rob2 = 0, 0
        for i in range(len(nums) - 1):
            rob1, rob2 = max(nums[i] + rob2, rob1), rob1

        withIdx0 = rob1

        rob1, rob2 = 0, 0
        for i in range(1, len(nums)):
            rob1, rob2 = max(nums[i] + rob2, rob1), rob1

        withIdx1 = rob1

        return max(withIdx0, withIdx1)
    
# Time Complexity: O(n)
# Space Complexity: O(1)