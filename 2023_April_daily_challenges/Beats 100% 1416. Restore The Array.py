# Beats 100% https://leetcode.com/problems/restore-the-array/solutions/3446952/beats-100-python-using-backtracking-and-caching/

# Time complexity O(n, min(n, len(str(k))). Space complexity O(n) only for caching.
class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        modulo = 10**9 + 7
        k_string = str(k)
        k_len = len(k_string)
        s_len = len(s)

        @functools.cache
        def dfs(start):
            if s_len - start == 0:
                return 1
            if s[start] == '0':
                return 0
            count = 0
            for index in range(start + 1, min(s_len, start + k_len) + 1):
                if index - start < k_len or int(s[start:index]) <= k:
                    count = (count + dfs(index)) % modulo
            return count

        return dfs(0)
