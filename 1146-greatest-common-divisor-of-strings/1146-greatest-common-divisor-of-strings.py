class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        ans = ""
        #get shorter string 
        st1_l = len(str1)
        st2_l = len(str2)
        print("len s1 ", st1_l )
        print("len s2 ", st2_l )

        if st2_l < st1_l:
            iterator = st2_l
            check1 = str2
            check2 = str1
        else: 
            iterator = st1_l
            check1 = str2
            check2 = str1
       

        for i in (range(iterator + 1, 0, -1)): #start bbackwards until find 
            temp_length = i 
            print(temp_length)
            if (len(check2) % temp_length == 0 and len(check1) % temp_length == 0) or temp_length == 1: 
                temp = check1[:i]

                #check str1
                temp1 = ""
                temp1_check = False
                while len(temp1) <= len(str1):
                    temp1 += temp
                    if temp1 == str1:
                        temp1_check = True
                
                #check str2
                temp2 = ""
                while len(temp2) <= len(str2):
                    temp2 += temp
                    if temp2 == str2:
                        if temp1_check == True: 
                            return temp
                    
                    
            else:
                continue
        
        return ans