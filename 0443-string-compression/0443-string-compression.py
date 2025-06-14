class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        read = 0
        length = len(chars)
        if length <= 1:
            return length
        

        while read < length: 
            curr = chars[read]
            count = 0 

            while read < length and chars[read] == curr: 
                count += 1
                read += 1
            
            chars[write] = curr
            write += 1
            if count > 1: 
                for digit in str(count): 
                    chars[write] = digit
                    write += 1
            
          
        
        del chars[write:]
        
        return len(chars)






        # s = chars[0]
        # seen = False
        # curr_letter = chars[0]
        # count  = 1
        # ans = []
        # #modify chars in placce 
        # for i in range(1,len(chars)): 
        #     #do normal 
        #     if not seen: #new char looking at
        #         if curr_letter == chars[i]: #conseccuitive repeating 
        #             seen = True
        #             curr_letter = chars[i]
        #             count += 1
        #             continue
        #         else: 
        #             curr_letter = chars[i]
        #             s += curr_letter
        #             count =  1
        #             continue
        #     else: 
        #         if curr_letter == chars[i]: 
        #             count += 1
        #             continue
        #         else: #new letter now
        #             s += str(count)
        #             count = 1 #reset count 
        #             curr_letter = chars[i]
        #             seen = False
        #             s += curr_letter
        
        # if seen == True: 
        #     s += str(count)

        # for i in range(len(chars)):
            


        # print("this is s ", s)
        # return len(ans)
        