# https://leetcode.com/problems/sliding-window-maximum/

# Here we use Monotonically Decreasing Queue.
# Time complexity is O(n). Space complexity O(k).
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque()
        result = []
        left, right = 0, 0
        for right in range(k):
            while len(d) and nums[d[-1]] < nums[right]:
                d.pop()
            d.append(right)
        result.append(nums[d[0]])
        left += 1
        right += 1
        while right < len(nums):
            if d[0] == left - 1:
                d.popleft()
            while len(d) and nums[d[-1]] < nums[right]:
                d.pop()
            d.append(right)
            result.append(nums[d[0]])
            left += 1
            right += 1
        return result
