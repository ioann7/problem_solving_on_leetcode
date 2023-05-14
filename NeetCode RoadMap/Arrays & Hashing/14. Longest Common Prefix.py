# https://leetcode.com/problems/longest-common-prefix/

# Time complexity O(n*m). Space same.
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = []
        index = 0
        min_length = min([len(s) for s in strs])
        while index < min_length:
            cur_char = strs[0][index]
            if any([cur_char != s[index] for s in strs]):
                break
            result.append(cur_char)
            index += 1
        return ''.join(result)
