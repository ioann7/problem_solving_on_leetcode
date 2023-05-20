# https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Binary search. time O(N*logN). space O(N).
        sub = [nums[0]]
        for num in nums:
            if num > sub[-1]:
                sub.append(num)
            else:
                sub[bisect_left(sub, num)] = num
        return len(sub)


        # Dynamic programming solution time O(n^2) space O(n).
        dp = [1] * len(nums)
        for index1 in reversed(range(len(nums))):
            for index2 in range(index1 + 1, len(nums)):
                if nums[index1] < nums[index2]:
                    dp[index1] = max(dp[index1], 1 + dp[index2])
        return max(dp)

        # dp - memoization time O(n^2) space O(n).
        @cache
        def dfs(index):
            if index == len(nums) - 1:
                return 1
            result = 1
            for i in range(index, len(nums)):
                if nums[index] < nums[i]:
                    result = max(result, 1 + dfs(i))
            return result

        result = 1
        for index in range(len(nums)):
            result = max(result, dfs(index))
        return result
