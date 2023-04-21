# https://leetcode.com/problems/subsets-ii/

from typing import List


# Time complexity O(n*2^n). Space complexity O(2^n).
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        current_array = []
        def dfs(index: int) -> None:
            if index >= len(nums):
                result.append(current_array.copy())
                return
            # decision with add num
            current_array.append(nums[index])
            dfs(index + 1)
            # decision withoud add num
            current_array.pop()
            next_index = index + 1
            while next_index < len(nums) and nums[next_index] == nums[index]:
                next_index += 1
            dfs(next_index)

        dfs(0)
        return result


# My first solution. Here is i am use more space.
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = {tuple()}

        def dfs(array: Tuple[int], index: int) -> None:
            if array not in result:
                result.add(array)
            index += 1
            if index == len(nums):
                return
            dfs(array + (nums[index],), index)
            dfs(array, index)

        for index, num in enumerate(nums):
            dfs((num,), index)
        return list(result)
