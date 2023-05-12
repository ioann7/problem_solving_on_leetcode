# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

# Time complexity O(n). Space complexity O(1).
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        index = len(arr) - 1
        cur_max = arr[index]
        arr[index] = -1
        index -= 1
        for index in range(index, -1, -1):
            cur_value = arr[index]
            arr[index] = cur_max
            if cur_value > cur_max:
                cur_max = cur_value
        return arr
