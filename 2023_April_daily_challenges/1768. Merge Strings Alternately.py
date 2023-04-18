# https://leetcode.com/problems/merge-strings-alternately/

# Time complexity O(n). Space complexity O(n), just for result.
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = [None] * (len(word1) + len(word2))
        index = 0
        for char1, char2 in zip(word1, word2):
            result[index] = char1
            index += 1
            result[index] = char2
            index += 1
        for left in range(index // 2, len(word1)):
            result[index] = word1[left]
            index += 1
        for right in range(index // 2, len(word2)):
            result[index] = word2[right]
            index += 1
        return ''.join(result)
