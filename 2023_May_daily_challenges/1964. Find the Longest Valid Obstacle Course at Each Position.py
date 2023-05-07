class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        result = []
        dp = [10**8] * (len(obstacles) + 1)
        for num in obstacles:
            index = bisect.bisect(dp, num)
            result.append(index + 1)
            dp[index] = num
        return result
