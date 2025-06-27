class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        #use DFS
        self.keys = []
        self.stack = [0]
        self.visited = []

        def dfs(node): 
            while self.stack: 
                curr = self.stack.pop()
                if curr not in self.visited: 
                    self.visited.append(curr)
                for i in range(len(rooms[curr])): 
                    if rooms[curr][i] not in self.visited: 
                        self.stack.append(rooms[curr][i])
            return


        dfs(rooms[0])
        return len(self.visited) == len(rooms)



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