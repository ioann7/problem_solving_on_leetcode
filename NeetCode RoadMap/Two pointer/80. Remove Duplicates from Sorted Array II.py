# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

# Time complexty O(n). Space complexity O(1).
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, paste = 0, 1
        current_num = nums[left]
        for right in range(len(nums)):
            if nums[right] != current_num:
                nums[paste] = nums[right]
                paste += 1
                left = right
                current_num = nums[left]
            elif right - left == 1:
                nums[paste] = nums[right]
                paste += 1
        return paste
