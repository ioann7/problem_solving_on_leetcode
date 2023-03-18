# https://leetcode.com/problems/group-anagrams/description/


from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for string in strs:
            key = str(sorted(string))
            result[key].append(string)
        return result.values()


# that solution without using defaultdict
class Solution:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for string in strs:
            key = str(sorted(string))
            if key in result:
                result[key].append(string)
            else:
                result[key] = [string]
        return result.values()
