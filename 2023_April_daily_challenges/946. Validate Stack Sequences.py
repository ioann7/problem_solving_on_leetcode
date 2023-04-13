# https://leetcode.com/problems/validate-stack-sequences/

from typing import List


# Time complexity O(n). Space complexity O(n).
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        pop_index = 0
        push_index = 0
        while pop_index < len(popped):
            while not stack or stack[-1] != popped[pop_index]:
                if push_index == len(pushed):
                    return False
                stack.append(pushed[push_index])
                push_index += 1
            stack.pop()
            pop_index += 1
        return True
