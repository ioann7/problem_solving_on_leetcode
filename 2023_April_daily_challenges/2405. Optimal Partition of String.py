# https://leetcode.com/problems/optimal-partition-of-string/


# Time complexity O(n). Space complexity O(1) because in english alphabet only 26 letters.
class Solution:
    def partitionString(self, s: str) -> int:
        cur_set = set()
        count = 0
        for char in s:
            if char in cur_set:
                cur_set = set()
                count += 1
            cur_set.add(char)
        count +=1
        return count
