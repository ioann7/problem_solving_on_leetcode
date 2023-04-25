# Time complexity O(n*logn). Space complexity O(n).
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
