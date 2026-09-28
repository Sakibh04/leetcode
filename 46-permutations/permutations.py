class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans, path, used = [], [], set()

        def backtrack():
            if len(path) == len(nums):
                ans.append(path[:])

            for i in range(len(nums)):
                if i in used:
                    continue

                used.add(i)
                path.append(nums[i])
                backtrack()
                path.pop()
                used.remove(i)

        backtrack()
        return ans