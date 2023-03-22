# https://leetcode.com/problems/top-k-frequent-elements

from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [value for value, times in Counter(nums).most_common(k)]


# without using collections.Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for number in nums:
            if number not in counter:
                counter[number] = 0
            counter[number] += 1
        return sorted(counter.keys(), key=lambda key: counter[key], reverse=True)[:k]
