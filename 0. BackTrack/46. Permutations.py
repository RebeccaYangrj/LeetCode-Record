class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        self.dfs(nums,[],res)
        return res
    def dfs(self,nums,path,res):
        while not nums:
            res.append(path)
            return 
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:],path+[nums[i]],res)
    # time complexity O(n!)
    # space complexity O(n!)
