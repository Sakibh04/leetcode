'''
Iterate through each element
If we hit 1, sink the surrounding island using dfs
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[0,1], [0, -1], [1,0], [-1,0]]
        def dfs(grid, row, col):
                if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != '1':
                    return
                
                grid[row][col] = '0'
                for dr, dc in directions:
                    newRow, newCol = row + dr, col + dc
                    dfs(grid, newRow, newCol) 
        
        n = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    dfs(grid, row, col)
                    n += 1

        return n
