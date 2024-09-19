# https://leetcode.com/problems/decode-string

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in s:
            # if i is not ']', then we push it to the stack
            if i != ']':
                stack.append(i)
            else:
                curr_str = ''
                # pop until we find '['
                while stack[-1] != '[':
                    curr_str = stack.pop() + curr_str

                # pop '['
                stack.pop()

                curr_num = ''
                # pop until we find a digit
                while stack and stack[-1].isdigit():
                    curr_num = stack.pop() + curr_num

                # multiply the current string with the current number
                curr_str = curr_str * int(curr_num)

                # push the decoded string back to the stack
                stack.append(curr_str)

        return "".join(stack)

# Time Complexity: O(n)
# Space Complexity: O(n)