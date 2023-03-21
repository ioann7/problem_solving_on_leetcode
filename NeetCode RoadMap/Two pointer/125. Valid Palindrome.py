# https://leetcode.com/problems/valid-palindrome/


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if not self.is_good_symbol(s[left]):
                left += 1
            elif not self.is_good_symbol(s[right]):
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True
    
    def is_good_symbol(self, symbol: str) -> bool:
        return (
            ord('a') <= ord(symbol) <= ord('z') or
            ord('A') <= ord(symbol) <= ord('Z') or
            ord('0') <= ord(symbol) <= ord('9')
        )
