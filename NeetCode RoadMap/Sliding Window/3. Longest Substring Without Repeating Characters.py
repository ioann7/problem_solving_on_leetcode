# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Time complexity O(n). Space complexity O(n).
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 1:
            return 0
        current_substring_set = set(s[0])
        max_unique = len(current_substring_set)
        left, right = 0, 1
        while right < len(s):
            if s[right] in current_substring_set:
                while s[left] != s[right]:
                    current_substring_set.remove(s[left])
                    left += 1
                current_substring_set.remove(s[left])
                left += 1
            else:
                current_substring_set.add(s[right])
                max_unique = max(max_unique, len(current_substring_set))
                right += 1
        return max_unique


# less code. time and space complexity the same.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_substring_set = set()
        left = 0
        result = 0
        for right in range(len(s)):
            while s[right] in current_substring_set:
                current_substring_set.remove(s[left])
                left += 1
            current_substring_set.add(s[right])
            result = max(result, right - left + 1)
        return result
