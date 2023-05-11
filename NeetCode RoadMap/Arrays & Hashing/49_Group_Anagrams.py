# https://leetcode.com/problems/group-anagrams/description/

# Time complexity O(n*m) where n is avg len(str) and m is len(strs). Space complexity O(m). 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            count = [0] * 26    # a - z
            for char in s:
                count[ord(char) - ord('a')] += 1
            result[tuple(count)].append(s)
        return result.values()


# My first solution
# Time complexity O((n*log(n))*m) where n is avg len(str) and m is len(strs). Space complexity O(m).
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for string in strs:
            key = str(sorted(string))
            result[key].append(string)
        return result.values()
