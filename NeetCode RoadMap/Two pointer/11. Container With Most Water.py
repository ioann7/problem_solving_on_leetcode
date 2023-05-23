# https://leetcode.com/problems/container-with-most-water/

# Time complexity O(n). Space complexity O(1).
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)
            if height[right] < height[left]:
                right -= 1
            else:
                left += 1
        return max_area
