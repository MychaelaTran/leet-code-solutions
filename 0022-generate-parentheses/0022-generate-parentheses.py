class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #use recussrsion 
        ans = []

        def generate(openP, closeP, curr): 
            if openP == 0 and closeP == 0: 
                ans.append(curr)
                return 
            
            if openP > 0: 
                generate(openP-1, closeP, curr + "(") #add open paranthesis 
            
            if openP < closeP:
                generate(openP, closeP - 1, curr + ")")
            
        generate(n,n, "")
        
        return ans




'''
n  = 1
()

n = 2
()()  /  (())  

n = 3
(open = 2, close = 3
(( open = 1 closer = 3       () open = 2 close = 2


'''
        