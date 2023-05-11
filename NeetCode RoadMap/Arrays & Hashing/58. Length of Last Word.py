# https://leetcode.com/problems/length-of-last-word/

# All solutions Time complexity O(n). Space O(1) except last.

# From end to start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        index = len(s) - 1
        while index >= 0 and s[index] == ' ':
            index -= 1
        while index >= 0 and s[index] != ' ':
            index -= 1
            count += 1
        return count


# From start to end
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        last_not_zero = 0
        for char in s:
            if char == ' ':
                count = 0
            else:
                count += 1
                last_not_zero = count
        return last_not_zero


# Using python cheats ;)
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
