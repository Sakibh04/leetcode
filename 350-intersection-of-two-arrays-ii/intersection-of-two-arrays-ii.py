from collections import Counter
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        c1 = Counter(nums1)
        c2 = Counter(nums2)

        result = []
        for num, count in c2.items():
            result.extend([num] * min(count, c1[num]))

        return result