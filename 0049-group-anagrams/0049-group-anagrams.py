class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        
        ans =[]
        
        myhash = defaultdict(list)
        
        for word in strs: 
            sortedWord = ''.join(sorted(word))    
            myhash[sortedWord].append(word)
        
        for key in myhash.keys(): 
            temp  = []
            for value in myhash[key]: 
                temp.append(value)
            ans.append(temp)
            
        return ans