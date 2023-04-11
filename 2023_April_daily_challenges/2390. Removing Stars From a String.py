# https://leetcode.com/problems/removing-stars-from-a-string/

# Time complexity is O(n). Space complexity is O(n).
class Solution:
    def removeStars(self, s: str) -> str:
        star_char = '*'
        stack = []
        for char in s:
            if char == star_char:
                stack and stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)


# My first solution. Time complexity O(n). Space complexity O(n).
class Solution:
    def removeStars(self, s: str) -> str:
        star_char = '*'
        stars_count = 0
        result = []
        for index in reversed(range(len(s))):
            if s[index] == star_char:
                stars_count += 1
            elif stars_count:
                stars_count -= 1
            else:
                result.append(s[index])
        return ''.join(reversed(result))
