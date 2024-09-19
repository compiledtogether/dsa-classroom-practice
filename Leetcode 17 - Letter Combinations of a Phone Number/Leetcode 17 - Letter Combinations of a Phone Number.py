# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        res: List[str] = []
        if not digits:
            return res

        def helper(curr: str, idx: int):
            if len(curr) == len(digits):
                res.append("".join(curr))
                return

            for i in mapping[digits[idx]]:
                # pick
                curr.append(i)
                helper(curr, idx+1)
                curr.pop()

        helper([], 0)
        return res

# Time Complexity: O(n * 4^n)
# Space Complexity: O(n)