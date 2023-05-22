# https://leetcode.com/problems/product-of-array-except-self/

# Time complexity O(n). Space complexity O(1), but O(n) for save result.
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        pre = 1
        post = 1
        for index in range(len(nums)):
            result[index] = pre
            pre *= nums[index]
        for index in range(len(nums) - 1, -1, -1):
            result[index] *= post
            post *= nums[index]
        return result


# Worse solution. But here is still Time complexity O(n). But Space complexity O(n).
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        result = [0] * len(nums)
        for index, num in enumerate(nums):
            prev = prefix[index - 1] if index > 0 else 1
            prefix[index] = prev * num
        for index in reversed(range(len(nums))):
            post = postfix[index + 1] if index < len(nums) - 1 else 1
            postfix[index] = post * nums[index]
        for index, num in enumerate(nums):
            pre = prefix[index - 1] if index > 0 else 1
            post = postfix[index + 1] if index < len(nums) - 1 else 1
            result[index] = pre * post
        return result


# My first answer on yandex interview, but in leetcode i can not use divison operator.
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        product = 1
        last_zero = None
        zeros = 0
        for index, num in enumerate(nums):
            if num == 0:
                zeros += 1
                last_zero = index
            else:
                product *= num
        if zeros == 1:
            result[last_zero] = product
            return result
        elif zeros == 0:
            for index, num in enumerate(nums):
                result[index] = product // num
        return result
