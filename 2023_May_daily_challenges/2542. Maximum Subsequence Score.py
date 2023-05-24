# https://leetcode.com/problems/maximum-subsequence-score/

# Time complexity O(NlogN). Space complexity O(n).
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [(num1, num2) for num1, num2 in zip(nums1, nums2)]
        nums = sorted(pairs, key=lambda e: e[1], reverse=True)
        cur_sum = 0
        cur_sum_heap = []
        for (num1, num2) in nums[:k]:
            cur_sum += num1
            heapq.heappush(cur_sum_heap, num1)
        result = cur_sum * num2
        for (num1, num2) in nums[k:]:
            cur_sum -= heapq.heappop(cur_sum_heap)
            heapq.heappush(cur_sum_heap, num1)
            cur_sum += num1
            result = max(result, cur_sum * num2)
        return result
