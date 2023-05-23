# https://leetcode.com/problems/kth-largest-element-in-a-stream/

# KthLargest.add() time complexity O(logN). Space complexity O(k).
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums)[-k:]
        self.k = k
        heapq.heapify(self.nums)

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        elif val > self.nums[0]:
            heapq.heappushpop(self.nums, val)
        return self.nums[0]
