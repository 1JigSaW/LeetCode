from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            max_1 = max(stones)
            stones.remove(max(stones))
            max_2 = max(stones)
            stones.remove(max(stones))
            if max_2 != max_1:
                stones.append(max_1 - max_2)
        if len(stones) == 0:
            return 0
        return stones[0]

stones = [2,7,4,1,8,1]
print(Solution().lastStoneWeight(stones))