# input range < 4 
# output all possible letter combinations: [combination1 combinnation2]
# backtrack method
# time complexity: Time Complexity : O(4^N*N), where N, is the length of input string. 4^N for building every possible string combination and N to form the string by joining each character.. Here, 4 is chosen assuming the worst case where each digit will be 7 or 9 and we would have 4*4*4*4 total string combinations.???
# space complexity: O(3(4)**n)

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return ""
        dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = []
        self.dfs(dic,0,digits,"",res)
        return res
    
    def dfs(self,dic,idx,digits,path,res):
        if len(path)==len(digits):
            res.append(path)
            return 
        for c in dic[digits[idx]]:
            self.dfs(dic,idx+1,digits,path+c,res)
