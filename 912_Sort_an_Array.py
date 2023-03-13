# https://leetcode.com/problems/sort-an-array/


from typing import List


def merge_sort(nums: List[int]) -> List[int]:
    len_nums = len(nums)
    mid = len_nums // 2
    if len_nums <= 1:
        return nums
    left_array = merge_sort(nums[:mid])
    right_array = merge_sort(nums[mid:])
    return merge(left_array, right_array)


def merge(left_array: List[int], right_array: List[int]) -> List[int]:
    result = [None] * (len(left_array)  + len(right_array))
    left, right, index = 0, 0, 0
    while left < len(left_array) and right < len(right_array):
        left_value = left_array[left]
        right_value = right_array[right]
        if left_value < right_value:
            result[index] = left_value
            left += 1
        else:
            result[index] = right_value
            right += 1
        index += 1

    while left < len(left_array):
        result[index] = left_array[left]
        left += 1
        index += 1

    while right < len(right_array):
        result[index] = right_array[right]
        right += 1
        index += 1

    return result




class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return merge_sort(nums)
