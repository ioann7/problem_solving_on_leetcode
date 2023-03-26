from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter_s = Counter(s)
        counter_t = Counter(t)
        for char, frequency in counter_s.items():
            if frequency != counter_t[char]:
                return False
        return True


# For fun
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


# Space complexity O(1). But time complexity O(nlogn)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
