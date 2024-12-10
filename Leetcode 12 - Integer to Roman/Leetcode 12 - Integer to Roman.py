# https://leetcode.com/problems/integer-to-roman

class Solution:
    def intToRoman(self, num: int) -> str:
        value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbol = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        romans = ''
    
        for i in range(len(value)):
            if(num==0):
                break
            count = num//value[i];        
            while count:
                romans += symbol[i]
                count -= 1
            num = num%value[i]
        
        return romans
    
# Time Complexity: O(1)
# Space Complexity: O(1)