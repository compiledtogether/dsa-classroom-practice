# https://leetcode.com/problems/subsets

# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         if len(nums) == 1:
#             return [[], nums]
#         res = self.subsets(nums[1:])
#         return res + list(map(lambda x: [nums[0]] + x, res))

# Time Complexity: O(2^n)
# Space Complexity: O(n)


class Solution:
    def helper(self, nums: List[int], idx: int, curr: List[int], res: List[List[int]]):
        if idx == len(nums):
            res.append(curr.copy()) # Do shallow copy, because curr is passed by reference
            return
        
        # include
        curr.append(nums[idx])
        self.helper(nums, idx+1, curr, res)
        curr.pop() # remove element as curr is passed by reference

        # exclude   
        self.helper(nums, idx+1, curr, res)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        curr: List[int] = []
        res: List[List[int]] = []

        self.helper(nums, 0, curr, res)

        return res
    
# Time Complexity: O(2^n)
# Space Complexity: O(n)