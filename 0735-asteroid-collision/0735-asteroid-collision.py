class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        #only have colision if one moves left and other right
        #ie if one moves pos first and neg second
        for rock in asteroids:
            while stack and stack[-1] > 0 and rock < 0:
                #if one on stack is smaller, pop it
                if stack[-1] < -rock:
                    stack.pop() 
                    continue #contnue to check if rock may collide again so dont append yet 
                elif stack[-1] == -rock: #if theyre the same pop it too 
                    stack.pop()
                break
            else:
                stack.append(rock)
                
        return stack


        