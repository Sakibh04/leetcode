import heapq
class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        rows, cols = len(heights), len(heights[0])


        minHeap = [[0, 0, 0]] #[difference, row, col]
        visited = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while minHeap:
            diff, r, c = heapq.heappop(minHeap)

            if (r, c) in visited:
                continue
            visited.add((r, c))
            if  (r,c) == (rows - 1, cols - 1):
                return diff

            for dr, dc in directions:
                newRow, newCol = r + dr, c + dc
                if (newRow < 0 or newCol < 0 or newRow == rows or newCol == cols or (newRow, newCol) in visited):
                    continue
                newDiff = max(diff, abs(heights[r][c] - heights[newRow][newCol]))
                heapq.heappush(minHeap, [newDiff, newRow, newCol])


