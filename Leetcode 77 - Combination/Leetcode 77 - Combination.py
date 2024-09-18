# https://leetcode.com/problems/combinations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def helper(res: List[List[int]], curr: List[int], idx: int, k: int):
            if len(curr) == k:
                res.append(curr.copy())
                return
            if idx > n:
                return

            # pick
            curr.append(idx)
            helper(res, curr, idx+1, k)
            curr.pop()

            # not pick
            helper(res, curr, idx+1, k)

        res: List[List[int]] = []
        curr: List[int] = []
        helper(res, curr, 1, k)
        return res
    
# Time Complexity: O(n*k)
# Space Complexity: O(k)