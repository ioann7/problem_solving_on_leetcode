# https://leetcode.com/problems/k-radius-subarray-averages/

# Time complexity O(n). Space complexity O(n).
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        result = [-1] * len(nums)
        window = ((k * 2) + 1)
        cur_sum = 0
        left, right = 0, 0
        if len(nums) < window:
            return result
        while right < window:
            cur_sum += nums[right]
            right += 1
        cur_index = k
        result[cur_index] = cur_sum // window
        cur_index += 1
        while right < len(nums):
            cur_sum += nums[right]
            cur_sum -= nums[left]
            result[cur_index] = cur_sum // window
            left += 1
            right += 1
            cur_index += 1
        return result
