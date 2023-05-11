# https://leetcode.com/problems/is-subsequence/


# Time complexity O(n). Space complexity O(1).
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left, right = 0, 0
        while left < len(s) and right < len(t):
            if t[right] == s[left]:
                left += 1
            right += 1
        return left == len(s)

# One more way
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_index = 0
        s_len = len(s)
        for char in t:
            if s_index < s_len and char == s[s_index]:
                s_index += 1
        if s_index == s_len:
            return True
        return False
