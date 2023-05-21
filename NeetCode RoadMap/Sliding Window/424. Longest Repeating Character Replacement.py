# https://leetcode.com/problems/longest-repeating-character-replacement/


# Time complexity O(n). Space complexity O(1) because alphabet has only 26 letters.
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        alphabet = defaultdict(int)
        left, right, max_window, max_freq = 0, 0, 0, 0
        for right in range(len(s)):
            alphabet[s[right]] += 1
            max_freq = max(max_freq, alphabet[s[right]])
            while (right - left + 1) - max_freq > k:
                alphabet[s[left]] -= 1
                left += 1
            max_window = max(max_window, right - left + 1)
        return max_window


# Time complexity O(26*n)=O(n). Space complexity O(1).
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        alphabet = defaultdict(int)
        left, right, max_window = 0, 0, 0
        for right in range(len(s)):
            alphabet[s[right]] += 1
            while (right - left + 1) - max(alphabet.values()) > k:
                alphabet[s[left]] -= 1
                left += 1
            max_window = max(max_window, right - left + 1)
        return max_window
