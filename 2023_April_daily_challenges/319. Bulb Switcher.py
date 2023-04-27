# https://leetcode.com/problems/bulb-switcher/

# Time complexity O(logn) for sqrt. Space complexity O(1).
class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(math.sqrt(n))
