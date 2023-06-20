# https://leetcode.com/problems/find-the-highest-altitude/

# Time complexity O(n). Space complexity O(1).
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        result = 0
        cur_altitude = 0
        for cur_gain in gain:
            cur_altitude += cur_gain
            result = max(result, cur_altitude)
        return result
