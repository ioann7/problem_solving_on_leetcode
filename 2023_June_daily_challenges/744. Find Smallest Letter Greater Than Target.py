# https://leetcode.com/problems/find-smallest-letter-greater-than-target/

# Time complexity O(logN). Space complexity O(1).
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letter = bisect_right(letters, ord(target), key=lambda e: ord(e))
        if letter == len(letters):
            return letters[0]
        return letters[letter]
