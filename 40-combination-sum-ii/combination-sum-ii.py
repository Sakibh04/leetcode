class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        ans, path = [], []
        candidates.sort()

        def backtrack(start, remaining):
            if remaining == 0:
                ans.append(path[:])

            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break
                if i > start and candidates[i] == candidates[i-1]:
                    continue

                path.append(candidates[i])
                backtrack(i+1, remaining - candidates[i])
                path.pop()

        backtrack(0, target)
        return ans
                