#dhiren 
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a == "0":
            return b
        if b == "0":
            return a
        answer = ""
        carry = 0
        addA = a[::-1]
        addB = b[::-1]
        if len(a) < len(b):
            #pad a with zero at front
            difference = len(b) - len(a)
            for i in range(difference):
                addA = addA + "0"   
        if len(b) < len(a):
            #pad b with zero at front 
            difference = len(a) - len(b)
            for i in range(difference):
                addB = addB + "0" 
        print(addA)
        print(addB)
        # ex 3 + 7 = 10
        # 3:  11
        # 7: 111
        # 10: 1010
        for a in range(len(addA)):
            for b in range(a, a+1):
                if a == b:
                    #addtion values when we have no carry = 0
                    if carry == 0: 
                        if addA[a] == "0" and addB[b] == "0":
                            answer = "0" + answer
                        
                        if addA[a] == "0" and addB[b] == "1":
                            print("entered when a = ",a)
                            answer = "1" + answer
                        
                        if addA[a] == "1" and addB[b] == "0":
                            answer = "1" + answer

                        if addA[a] == "1" and addB[b] == "1":
                            answer = "0" + answer
                            carry = 1

                    #addition values when we have a carry = 1
                    else:
                        if addA[a] == "0" and addB[b] == "0":
                            answer = "1" + answer
                            carry = 0 
                        
                        if addA[a] == "0" and addB[b] == "1":
                            answer = "0" + answer
                        
                        if addA[a] == "1" and addB[b] == "0":
                            answer = "0" + answer

                        if addA[a] == "1" and addB[b] == "1":
                            answer = "1" + answer
                    
        
        if carry == 1:
            answer = "1" + answer

        return answer

                

