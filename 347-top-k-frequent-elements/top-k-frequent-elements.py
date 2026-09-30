from collections import defaultdict
from operator import itemgetter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency: Dict[int, int] = defaultdict(int)
        most_frequent = []
        for num in nums:
           frequency[num] += 1
        
        sorted_frequencies = sorted(frequency.items(), key=itemgetter(1), reverse=True)
        
        for i in range(k):
            most_frequent.append(sorted_frequencies[i][0])

        return most_frequent
        


        
