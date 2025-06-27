class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        seen = set()
        provinces = 0

        for i in range(n):
            if i not in seen: #have this for when done searchign a province you have to search the next
                stack = [i]
                while stack:
                    curr = stack.pop()
                    if curr not in seen:
                        seen.add(curr)
                        for j in range(n):
                            if isConnected[curr][j] == 1 and j not in seen:
                                stack.append(j)
                provinces += 1 #add provinve when done one break of while loop

        return provinces
