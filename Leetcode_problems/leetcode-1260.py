class Solution:
    def shiftGrid(self, grid,k):
        m = len(grid)
        n = len(grid[0])
        total = m * n
        k %= total
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                y = i * n + j
                x = (y + k) % total
                r = x // n
                c = x % n
                ans[r][c] = grid[i][j]
        return ans
grid,k = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], 4
print(Solution().shiftGrid(grid,k))