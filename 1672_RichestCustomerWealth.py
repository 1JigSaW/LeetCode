from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxx = 0
        summ = 0
        for account in accounts:
            for bank in account:
                summ += bank
            if maxx < summ:
                maxx = summ
            summ = 0
        return maxx

print(Solution().maximumWealth([[1,2,3], [4,5,6]]))