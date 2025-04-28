class Solution:
    def romanToInt(self, s: str) -> int:
        marker = True
        total = 0
        for i in range(len(s)):
            if marker:
                match s[i]:
                    case "I":
                        if i != len(s) -1:
                            if s[i+1] == "V":
                                total += 4 
                                marker = False
                            elif s[i+1] == "X":
                                total += 9
                                marker = False
                            else: total += 1 
                        else: total += 1
                    case "V":
                        total += 5
                    case "X":
                        if i != len(s) -1:
                            if s[i+1] == "L":
                                total += 40
                                marker = False
                            elif s[i+1] == "C":
                                total += 90
                                marker = False
                            else: total += 10
                        else: 
                            total += 10
                    case "L":
                        total += 50
                    case "C":
                        if i != len(s) -1:
                            if s[i+1] == "D":
                                total += 400
                                marker = False
                            elif s[i+1] == "M":
                                total += 900
                                marker = False
                            else: total += 100
                        else: total += 100
                    case "D":
                        total += 500
                    case "M":
                        total += 1000
            else:
                marker = True
                continue
        return total 

        