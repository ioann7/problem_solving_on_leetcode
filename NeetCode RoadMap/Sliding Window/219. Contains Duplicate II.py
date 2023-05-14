# https://leetcode.com/problems/contains-duplicate-ii/

# Time complexity O(n). Space complexity O(k).
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set((nums[0],))
        left = 0
        for right in range(1, len(nums)):
            if right > k:
                window.remove(nums[left])
                left += 1
            if nums[right] in window:
                return True
            window.add(nums[right])
