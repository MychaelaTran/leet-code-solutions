class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1: 
            return [[1]]
 
        
        answer = [[1]]
        count = 1 
        for i in range(1, numRows): #1 bc handled [1] already
            count += 1
            temp = []
            for j in range(0, count):
                #first and last are always 1
                if j == 0:
                    temp.append(1)
                    continue

                if j == (count -1):
                    temp.append(1)
                    continue

                temp.append(answer[i-1][j] + answer[i-1][j-1])
               # [ [1]  [1,1]   [1,2,1]   [1,3,3,1]    ]

            answer.append(temp)
            

        return answer







        