class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        distances = []
        for x,y in points:
            distances.append([-1 * (x**2 + y**2),x,y])

        heapq.heapify(distances)
        while len(distances) > k:
            heapq.heappop(distances)

        return [[x, y] for distance, x, y in distances]        