# https://leetcode.com/problems/jump-game-ii

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps, current, farthest = 0,0,0

        for i in range(n-1):
            farthest = max(farthest, i + nums[i])
            if i == current:
                jumps += 1
                current = farthest

        return jumps
    
# Time Complexity: 0(n)
# Space Complexity: 0(1)