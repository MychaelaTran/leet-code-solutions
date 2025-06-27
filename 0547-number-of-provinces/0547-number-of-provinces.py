class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 1
        seen = set()
        stack = [0]

        while stack:
            curr = stack.pop()
                
            
            for i in range(len(isConnected[curr])): 
                if isConnected[curr][i] == 1 and i not in seen: 
                    stack.append(i)
                    seen.add(curr)
                    

            if not stack and len(seen) != len(isConnected): 
                # add other province next one to stack to traverse and do provinsces += 1
                provinces += 1
                for i in range(len(isConnected)): 
                    if i not in seen: 
                        stack.append(i)
                        break

        return provinces

        