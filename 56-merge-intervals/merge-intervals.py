from operator import itemgetter
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=itemgetter(0))
        result = [intervals[0]]

        for start, end in intervals[1:]:
            last_end = result[-1][-1]
            if start <= last_end:
                result[-1][1] = max(result[-1][1], end)
            else:
                result.append([start, end])

        return result