class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if not m or not n:
            return 0
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j-1]
                print(cur)
        return cur[-1]

m = 3
n = 7
print(Solution().uniquePaths(m,n))