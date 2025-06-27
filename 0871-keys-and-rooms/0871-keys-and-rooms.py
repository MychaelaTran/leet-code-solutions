class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        #use DFS
        stack = [0]
        visited = set()

        while stack: 
            curr = stack.pop()
            if curr not in visited: 
                visited.add(curr)
            for i in range(len(rooms[curr])): 
                if rooms[curr][i] not in visited: 
                    stack.append(rooms[curr][i])

        return len(visited) == len(rooms)



'''
 rooms = [[1],[2],[3],[]]
 keys = []
 stack = [0]
 visted = []

 1. curr = 0
 visited = [0]
 i = 1
 rooms[0][0]
 stack = [1]
 keys = [1]

 2. 
 curr = 1
 visited = [0,1]
 keys = [1,2]
 stack = [2]

 3.

 stack = [3]
 keys = [1,2,3]



 '''