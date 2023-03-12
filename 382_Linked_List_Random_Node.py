# https://leetcode.com/problems/linked-list-random-node/


import random
from typing import Optional, Tuple


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.last = head
        self.last_index = 0

    def set_last_node_and_length(self) -> Tuple[ListNode, int]:
        while self.last.next:
            self.last = self.last.next
            self.last_index += 1

    def get_random(self) -> int:
        self.set_last_node_and_length()
        random_index = random.randint(0, self.last_index)
        current_index = 0
        head = self.head
        while current_index < random_index:
            head = head.next
            current_index += 1
        return head.val

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.get_random()
