class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        #need to use BFS 
        ans = 0
        edges = set()
        visited = set()
        visited.add(0)
        neighbours = defaultdict(list)
        for a,b in connections:
            neighbours[a].append(b)
            neighbours[b].append(a)
            edges.add((a,b))
        
        #gives us a node and all its neighbours
        #ex 1: 
        # { 0: [1,4], 1: [0,3], 2: [3], 3: [2,1], 4: [0,5], 5: [4]   }

        curr = [0]
        while curr:
            new_curr = []
            for city in curr:  #goes through "queue"
                for n in neighbours[city]: #neightbours of 0, 1 and 4
                    if n not in visited: 
                        visited.add(n)
                        if (n, city) not in edges: #if (1,0) not in edges (ITS NOT)
                            ans += 1 #add since need to rever and curr have (0,1)
                        new_curr.append(n)
            curr = new_curr
        return ans
        



        

        