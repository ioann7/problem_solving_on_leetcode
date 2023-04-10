# https://leetcode.com/problems/valid-parentheses/

# Time complexity is O(N). Space complexity is O(N).
class Solution:
    def isValid(self, s: str) -> bool:
        closed_brackets = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        stack = []
        for char in s:
            if char not in closed_brackets:
                stack.append(char)
            else:
                bracket = stack.pop() if stack else None
                if closed_brackets[char] != bracket:
                    return False
        if stack:
            return False
        return True
