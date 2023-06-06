# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/

# Time complexity O(NlogN). Space complexity O(N).
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        new_arr = sorted(arr)
        difference = new_arr[1] - new_arr[0]
        for index in range(2, len(new_arr)):
            if new_arr[index] - new_arr[index - 1] != difference:
                return False
        return True
