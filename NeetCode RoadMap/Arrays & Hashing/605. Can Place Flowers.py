# https://leetcode.com/problems/can-place-flowers/description/

from typing import List


# Here is time complexity O(n) and additional space complexity O(1)
# And i am not changing `flowerbed`
class Solution:
    def can_place_flowers(self, flowerbed: List[int], n: int) -> bool:
        can_be_planted = 0
        left = -1
        right = 0
        while right < len(flowerbed):
            if flowerbed[right] == 0:
                zeros = (right - left) + 1
                if zeros == 3:
                    can_be_planted += 1
                    left += 2
                right += 1
            else:
                right += 1
                left = right
        zeros = (right - left) + 1
        if zeros == 3:
            can_be_planted += 1
        if can_be_planted >= n:
            return True
        return False


# Here is prettier solution but using additional space complexity O(n)
class Solution:
    def can_place_flowers(self, flowerbed: List[int], n: int) -> bool:
        can_be_planted = 0
        new_flowerbed = [0] + flowerbed + [0]
        for index in range(1, len(new_flowerbed) - 1):
            if not any((new_flowerbed[index - 1], new_flowerbed[index], new_flowerbed[index + 1])):
                can_be_planted += 1
                new_flowerbed[index] = 1
        if can_be_planted >= n:
            return True
        return False
