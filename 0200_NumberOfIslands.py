from typing import List

class Solution:
    # def numIslands(self, grid: List[List[str]]) -> int:
    #     island = 0
    #     first_island = 0
    #     for i in range(len(grid)):
    #         for j in range(len(grid[0])):
    #             if i == 0:
    #                 if j == 0:
    #                     if grid[i][j] == '1':
    #                         first_island = 1
    #                         continue
    #                 elif j == len(grid[0])-1:
    #                     if grid[i][j] == '1':
    #                         first_island = 1
    #                         if grid[i][j-1] == '0':
    #                             island += 1
    #                             continue
    #                 else:
    #                     if grid[i][j] == '1':
    #                         first_island = 1
    #                         if grid[i][j-1] == '0':
    #                             island += 1
    #                             continue
    #             elif i == len(grid)-1:
    #                 if j == 0:
    #                     if grid[i][j] == '1':
    #                         first_island = 1
    #                         if grid[i-1][j] == '0':
    #                             island += 1
    #                             continue
    #                 elif j == len(grid[0])-1:
    #                     if grid[i][j] == '1':
    #                         first_island = 1
    #                         if grid[i-1][j] == '0' and grid[i][j-1] == '0':
    #                             island += 1
    #                             continue
    #                 else:
    #                     if grid[i][j] == '1':
    #                         first_island = 1
    #                         if grid[i-1][j] == '0' and grid[i][j-1] == '0':
    #                             island += 1
    #                             continue
    #             else:
    #                 if j == 0:
    #                     if grid[i][j] == '1':
    #                         first_island = 1
    #                         if grid[i-1][j] == '0':
    #                             island += 1
    #                             continue
    #                 elif j == len(grid[0])-1:
    #                     if grid[i][j] == '1':
    #                         first_island = 1
    #                         if grid[i-1][j] == '0' and grid[i][j-1] == '0':
    #                             island += 1
    #                             continue
    #                 else:
    #                     if grid[i][j] == '1':
    #                         first_island = 1
    #                         if grid[i-1][j] == '0' and grid[i][j-1] == '0':
    #                             island += 1
    #                             continue         
    #     return island + first_island

        def numIslands(self, grid):
            if not grid:
                return 0
                
            count = 0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == '1':
                        self.dfs(grid, i, j)
                        count += 1
            return count

        def dfs(self, grid, i, j):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
                return
            grid[i][j] = '#'
            self.dfs(grid, i+1, j)
            self.dfs(grid, i-1, j)
            self.dfs(grid, i, j+1)
            self.dfs(grid, i, j-1)

grid = [["0","0","0","0","0","0","1"]]
print(Solution().numIslands(grid))