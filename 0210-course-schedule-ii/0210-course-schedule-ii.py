class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #topological graph sort with dfs and return vertices in reverse postorder
        #only have topologival if DAG 
        #get sink vertex (no outgoing)
        ans = []
        seen = set()
        path = set()
        prereqs = {course:[] for course in range(numCourses)}
        for course, prereq in prerequisites:
            prereqs[course].append(prereq)


        def dfs(course): 
            if course in path: #cycle
                return False
            if course in seen: #already visited , done here
                return True
            
            path.add(course)
            for prereq in prereqs[course]: 
                if dfs(prereq) == False: 
                    return False
            path.remove(course) #backtrack 
            seen.add(course)
            ans.append(course)
            return True 
        
        for course in range(numCourses): 
            if dfs(course) == False: 
                return []
        return ans 






        