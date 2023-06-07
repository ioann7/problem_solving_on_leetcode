# https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        a, b, c = reversed(bin(a)[2:]), reversed(bin(b)[2:]), reversed(bin(c)[2:])
        result = 0
        for ai, bi, ci in itertools.zip_longest(a, b, c, fillvalue='0'):
            if ci == '1' and ai == '0' and bi == '0':
                result += 1
            elif ci == '0':
                if ai == '1':
                    result += 1
                if bi == '1':
                    result += 1
        return result
