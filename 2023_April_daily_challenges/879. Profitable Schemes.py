# https://leetcode.com/problems/profitable-schemes/

class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        modulo = 10**9 + 7
        dp = defaultdict(int)

        for m in range(n + 1):
            dp[(len(group), m, minProfit)] = 1

        for i in range(len(group) - 1, -1, -1):
            for m in range(n + 1):
                for p in range(minProfit + 1):
                    dp[(i, m, p)] = dp[(i + 1, m, p)]
                    if m + group[i] <= n:
                        dp[(i, m, p)] += (
                            dp[(
                                i + 1,
                                m + group[i],
                                min(minProfit, p + profit[i])
                            )] % modulo
                        )
        return dp[(0, 0, 0)] % modulo


class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        modulo = 10**9 + 7
        dp = {}

        def backtrack(bandits: int, current_profit: int, index: int) -> None:
            if index >= len(group):
                return 1 if current_profit >= minProfit else 0
            if (bandits, current_profit, index) in dp:
                return dp[(bandits, current_profit, index)]
            dp[(bandits, current_profit, index)] = backtrack(
                bandits,
                current_profit,
                index + 1,
            )
            new_bandits = bandits - group[index]
            if new_bandits >= 0:
                dp[(bandits, current_profit, index)] += backtrack(
                    new_bandits,
                    current_profit + profit[index],
                    index + 1,
                ) % modulo
            return dp[(bandits, current_profit, index)]

        return backtrack(n, 0, 0)
