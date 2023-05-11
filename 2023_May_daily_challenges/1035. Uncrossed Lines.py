# https://leetcode.com/problems/uncrossed-lines/

# Time complexity O(n*m). Space complexity for caching O(n*m).
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:

        @cache
        def dfs(i, j):
            if i == len(nums1) or j == len(nums2):
                return 0
            if nums1[i] == nums2[j]:
                return 1 + dfs(i + 1, j + 1)
            else:
                return max(dfs(i + 1, j), dfs(i, j + 1))

        return dfs(0, 0)


# Here is same, but i am using my own caching
class Solution:
        cache = {}

        def dfs(i, j):
            if i == len(nums1) or j == len(nums2):
                return 0
            if (i, j) in cache:
                return cache[(i, j)]
            if nums1[i] == nums2[j]:
                cache[(i, j)] = 1 + dfs(i + 1, j + 1)
            else:
                cache[(i, j)] = max(dfs(i + 1, j), dfs(i, j + 1))
            return cache[(i, j)]

        return dfs(0, 0)
