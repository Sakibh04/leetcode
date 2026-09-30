class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = None
        count = 0
        for value in nums:
            if count == 0:
                candidate = value
            if value == candidate:
                count += 1
            else:
                count -= 1

        return candidate

        