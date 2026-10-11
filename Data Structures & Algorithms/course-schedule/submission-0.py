class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        inorder = [0] * (numCourses)

        for i, j in prerequisites:
            graph[i].append(j)
            inorder[j] += 1

        order = []
        q = deque()

        for i in range(len(graph)):
            if inorder[i] == 0:
                q.append(i)
        
        while q:
            curr = q.popleft()
            order.append(curr)

            for nb in graph[curr]:
                inorder[nb] -= 1

                if inorder[nb] == 0:
                    q.append(nb)

        return len(order) == numCourses
