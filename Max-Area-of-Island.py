# Time:  O(m * n)
# Space: O(m * n), the max depth of dfs may be m * n


class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j]:
                grid[i][j] = 0
                return 1+dfs(i-1, j)+dfs(i, j+1)+dfs(i+1, j)+dfs(i, j-1)
            return 0
        aeras = [dfs(i, j) for i in range(m) for j in range(n) if grid[i][j]]
        return max(aeras) if aeras else 0