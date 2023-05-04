# https://leetcode.com/problems/dota2-senate/

from collections import deque


# Time complexity O(n). Space complexity O(n).
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_queue = deque()
        d_queue = deque()
        for index, s in enumerate(senate):
            if s == 'R':
                r_queue.append(index)
            else:
                d_queue.append(index)

        while r_queue and d_queue:
            if r_queue[0] > d_queue[0]:
                d_queue.popleft()
                r_queue.append(r_queue.popleft() + len(senate))
            else:
                r_queue.popleft()
                d_queue.append(d_queue.popleft() + len(senate))
        if r_queue:
            return 'Radiant'
        return 'Dire'
