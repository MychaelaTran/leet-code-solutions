class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #find edge that makes cycle union find
        parent = [i for i in range(len(edges)+ 1)] #+1 bc less edges
        rank = [1 for i in range(len(edges) + 1)]


        def find(x):
            #path compression
            while x != parent[x]: #parent doesnt equal itself 
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x #root
        
        def union(n1, n2): 
            n1_p = find(n1)
            n2_p = find(n2)

            if n1_p == n2_p: 
                return False #redundant connection 
            
            #conect by rank
            if rank[n1_p] > rank[n2_p]: 
                rank[n1_p] += rank[n2_p]
                parent[n2_p] = n1_p
            else :
                rank[n2_p] += rank[n1_p]
                parent[n1_p] = n2_p
            return True

        for n1, n2 in edges: 
            if union(n1, n2) == False: 
                return [n1, n2]

            


        
