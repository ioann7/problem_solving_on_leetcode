# https://leetcode.com/problems/k-closest-points-to-origin/

# Time complexity O(N + KlogN) that is better than O(NlogN) if we using default sorting. Space complexity O(n).
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [((x**2 + y**2), (x, y)) for x, y in points]
        heapq.heapify(distances)
        return [heapq.heappop(distances)[1] for _ in range(k)]
