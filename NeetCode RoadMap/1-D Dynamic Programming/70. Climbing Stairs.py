# https://leetcode.com/problems/climbing-stairs


# Time complexity O(n). Space complexity O(1).
class Solution:
    def climbStairs(self, n: int) -> int:
        prev_prev, prev = 1, 1
        for _ in range(2, n + 1):
            temp = prev_prev + prev
            prev_prev = prev
            prev = temp
        return prev


# my first solution. Time complexity O(n). Space complexity O(n) + O(n), for caching and recursion.
class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [None] * (n + 1)
        current_stair = n
        cache[current_stair] = 1
        self.count_climb_stairs(n, current_stair - 1, cache)
        return cache[0]

    def count_climb_stairs(self, n: int, current_stair: int, cache: List[int]) -> None:
        first, second = 0, 0
        if current_stair + 1 <= n:
            first = cache[current_stair + 1]
        if current_stair + 2 <= n:
            second = cache[current_stair + 2]
        cache[current_stair] = first + second
        if current_stair == 0:
            return
        self.count_climb_stairs(n, current_stair - 1, cache)
