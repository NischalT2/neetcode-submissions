class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        curr_list = set()
        def dfs(crs):
            if crs in curr_list:
                return False
            if preMap[crs] == []:
                return True
            
            curr_list.add(crs)
            for j in preMap[crs]:
                if not dfs(j):
                    return False
                
            curr_list.remove(crs)
            preMap[crs] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True

