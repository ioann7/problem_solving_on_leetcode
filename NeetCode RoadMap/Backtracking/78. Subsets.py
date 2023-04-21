# https://leetcode.com/problems/subsets/

from typing import List


# Time complexity is O(n*2^n). Space complexity O(2^n). Where n is length of nums.
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        current_array = []
        def dfs(index: int) -> None:
            if index >= len(nums):
                result.append(current_array.copy())
                return
            # decision with add num
            current_array.append(nums[index])
            dfs(index + 1)

            # decision without add num
            current_array.pop()
            dfs(index + 1)

        dfs(0)
        return result


# My first solution. Here i am using more space.
class Solution:
    def subsets(self, nums: List[int]) -> List[Tuple[int]]:
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
