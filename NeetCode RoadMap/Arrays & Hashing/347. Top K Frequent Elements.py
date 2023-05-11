# https://leetcode.com/problems/top-k-frequent-elements

# Time complexity O(n). Space complexity O(n).
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        frequencies = [[] for _ in range(len(nums) + 1)]
        for number, frequency in counter.items():
            frequencies[frequency].append(number)
        result = []
        for frequency in reversed(frequencies):
            for number in frequency:
                result.append(number)
                if len(result) == k:
                    return result
