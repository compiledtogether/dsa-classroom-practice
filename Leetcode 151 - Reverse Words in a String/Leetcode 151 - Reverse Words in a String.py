# https://leetcode.com/problems/reverse-words-in-a-string

class Solution:
    def reverseWords(self, s: str) -> str:
        strippedList = list(filter(lambda item: item.strip() != "", s.split(" ")))

        left = 0
        right = len(strippedList) - 1

        while left < right:
            strippedList[left], strippedList[right] = strippedList[right], strippedList[left]
            left += 1
            right -= 1

        return " ".join(strippedList)
        
# Time Complexity: O(n)
# Space Complexity: O(n)