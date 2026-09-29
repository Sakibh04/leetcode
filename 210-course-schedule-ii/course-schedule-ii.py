class Solution:
    '''
    Rather than course schedule where you return true if preMap[crs] == [] returns True, we append the course to the result array
    '''
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        preMap = {i:[] for i in range(numCourses)}
        res = []
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visited, finished = set(), set()
        def dfs(crs):
            if crs in visited:
                return False
            if crs in finished:
                return True

            visited.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False 

            visited.remove(crs)
            finished.add(crs)
            preMap[crs] = []
            res.append(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs): return []

        return res