# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

# Time complexity O(n). Space complexity O(1).
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(('a', 'e', 'i', 'o', 'u'))
        max_vowels = 0
        left, right = 0, 0
        cur_vowels = 0
        while right < k:
            if s[right] in vowels:
                cur_vowels += 1
            right += 1
        max_vowels = cur_vowels
        while right < len(s):
            if s[right] in vowels:
                cur_vowels += 1
            if s[left] in vowels:
                cur_vowels -= 1
            max_vowels = max(max_vowels, cur_vowels)
            left += 1
            right += 1
        return max_vowels
