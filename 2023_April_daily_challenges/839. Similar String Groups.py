# https://leetcode.com/problems/similar-string-groups/

from typing import List


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        visited = [False] * len(strs)
        groups = 0
        for i in range(len(strs)):
            if not visited[i]:
                groups += 1
                self.dfs(i, visited, strs)
        return groups

    def dfs(self, i: int, visited: List[bool], strs: List[str]) -> None:
        visited[i] = True
        for j in range(len(strs)):
            if visited[j]:
                continue
            if self.is_similar(strs[i], strs[j]):
                self.dfs(j, visited, strs)

    def is_similar(self, str1: str, str2: str) -> bool:
        count = 0
        for char1, char2 in zip(str1, str2):
            if char1 != char2:
                count += 1
        return count == 0 or count == 2
