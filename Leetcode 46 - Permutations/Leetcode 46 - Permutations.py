# https://leetcode.com/problems/permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(res: List[List[int]], idx: int):
            # base condition
            if idx == len(nums):
                res.append(nums.copy())
                return

            for i in range(idx, len(nums)):
                nums[idx], nums[i] = nums[i], nums[idx]
                helper(res, idx+1)
                nums[idx], nums[i] = nums[i], nums[idx]

        res: List[List[int]] = []
        helper(res, 0)
        return res
            

# Time Complexity: O(n!)
# Space Complexity: O(n)