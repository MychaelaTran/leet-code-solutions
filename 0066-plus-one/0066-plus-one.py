class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        change = digits[0]
        if change < 9:
            digits[0] += 1
            digits.reverse()
        else: 
            digits[0] = 0
            if len(digits) > 1 and digits[1] != 9: 
                digits[1] += 1
                digits.reverse()
            elif len(digits) > 1 and digits[1] == 9:
                return self.helper(digits)
            else: 
                digits.append(1)
                digits.reverse()


        return digits


    def helper(self,digits): #count is the numbber of 9s we changed to zero 
        for i in range(1, len(digits)):
            if digits[i] == 9 and i != 1: 
                break
            elif digits[i] == 9 and i == 1: 
                digits[i] = 0
                if i != len(digits) -1 :
                    digits[i+1] += 1
                else: digits.append(1)

            elif digits[i] == 10: 
                if i != len(digits) -1:
                    digits[i] = 0
                    digits[i + 1] += 1
                else: 
                    digits[i] = 0
                    digits.append(1)
            else: 
                break
        digits.reverse()
        return digits
                
        
                



            #   elif len(digits) >= 2 and digits[0] == 9 and digits[1] == 9:
            # digits[0] = 0
            # digits[1] = 0
            # if len(digits) > 2: 
            #     digits[2] += 1
            #     if digits[2] == 10: 
            #         digits[2] == 0
            #         plusOne()

            #     digits.reverse()
            # else: 
            #     digits.append(1)
            #     digits.reverse()