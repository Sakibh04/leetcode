class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        negStones = [-x for x in stones]
        maxHeap = heapq.heapify(negStones)

        while len(negStones) > 1:
            stone1 = -1 * heapq.heappop(negStones)
            stone2 = -1 * heapq.heappop(negStones)
            if stone1 > stone2:
                heapq.heappush(negStones, -1 * (stone1 - stone2))
            elif stone2 > stone1:
                heapq.heappush(negStones, -1 * (stone2 - stone1))
            
        if negStones:
            return -1 * negStones[0]
        else:
            return 0