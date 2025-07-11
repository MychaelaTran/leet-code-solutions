from collections import deque, defaultdict
from typing import List
'''
Kahn's algo for topological sort: 
Kahn's Algorithm works by repeatedly finding vertices with no incoming edges, removing them from the graph, and updating the incoming edges of the vertices connected from the removed removed edges. This process continues until all vertices have been ordered.


'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)        #b: [a, c] b is a pre-req for a and c 
        in_degree = [0] * numCourses     #num of prereqs each course has

        for course, pre_req in prerequisites:
            graph[pre_req].append(course)           #pre_req is a prerequisite for course
            in_degree[course] += 1            #add to in-deg of course (in is how many pre=req has)

        q = deque([i for i in range(numCourses) if in_degree[i] == 0])
        completed = 0

        while q:
            course = q.popleft()
            completed += 1

            for neighbor in graph[course]: #looks at all courses that course is a pre-req for 
                in_degree[neighbor] -= 1 #minus becase we can take the neighbour's courses since we have the course taken 
                if in_degree[neighbor] == 0:
                    q.append(neighbor) #add to q once all pre-reqs taklen 

        return completed == numCourses
