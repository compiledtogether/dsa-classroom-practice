# https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        unique = set()
        for j in range(len(nums)):
            if not nums[j] in unique:
                unique.add(nums[j])
                nums[i] = nums[j]
                i += 1
        return i
    
# Time complexity: O(n)
# Space complexity: O(n)