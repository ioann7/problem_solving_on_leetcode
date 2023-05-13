# https://leetcode.com/problems/longest-turbulent-subarray/

# Time complexity O(n). Space complexity O(1).
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        cur_subarray = 1
        max_subarray = 1
        prev_most = True
        for index in range(1, len(arr)):
            if arr[index] == arr[index - 1]:
                cur_subarray = 1
                prev_most = True
            elif prev_most:
                if arr[index] < arr[index - 1]:
                    cur_subarray += 1
                    prev_most = False
                else:
                    cur_subarray = 2
            else:
                if arr[index] > arr[index - 1]:
                    cur_subarray += 1
                    prev_most = True
                else:
                    cur_subarray = 2
            max_subarray = max(max_subarray, cur_subarray)
        return max_subarray
