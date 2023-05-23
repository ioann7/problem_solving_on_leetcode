# https://leetcode.com/problems/trapping-rain-water/

# Time complexity O(n+n+n+n/2+n/2+n/2+n/2)=O(n). Space complexity (1).
class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        left = 0
        max_index = height.index(max(height))
        for right in range(max_index + 1):
            if height[right] >= height[left]:
                for temp in range(right - 1, left, -1):
                    result += height[left] - height[temp]
                left = right
        left = len(height) - 1
        for right in range(len(height) - 1, max_index - 1, -1):
            if height[right] >= height[left]:
                for temp in range(right + 1, left):
                    result += height[left] - height[temp]
                left = right
        return result
