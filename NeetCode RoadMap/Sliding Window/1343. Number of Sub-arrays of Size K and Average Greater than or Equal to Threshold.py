# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/

# Time complexity O(n). Space complexity O(1).
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        result = 0
        window_sum = 0
        left = 0
        for right in range(k):
            window_sum += arr[right]
        if window_sum / k >= threshold:
                result += 1
        for right in range(k, len(arr)):
            window_sum -= arr[left]
            left += 1
            window_sum += arr[right]
            if window_sum / k >= threshold:
                result += 1
        return result
