# https://leetcode.com/problems/range-sum-query-immutable/

# Time complexity for get sumRange O(1). Space complexity O(n).
class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = []
        total = 0
        for num in nums:
            total += num
            self.prefix_sum.append(total)      

    def sumRange(self, left: int, right: int) -> int:
        left_sum = self.prefix_sum[left - 1] if left > 0 else 0
        right_sum = self.prefix_sum[right]
        return right_sum - left_sum
