class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # find the first item which is smaller than the next one
        # 封装成一个函数：finder
        k = self.finder(len(nums)-1,0,nums)
        if k == 0: 
            nums.reverse() 
            return 
        else: k -=1
        
        
        # find the number which is the next larger one than the found number 
        # 封装成一个函数：changer
        self.changer(len(nums)-1,k,nums)
        
        # reverse the left part
        # 封装成一个函数：reverser
        self.reverser(k+1,len(nums)-1,nums)
        return 
        # time complexity : O(n)
        # space complexity : O(1)
             
    def finder(self,i,l,nums):
        while i>l and nums[i]<=nums[i-1]:
            i-=1 
        return i
    
    def changer(self,j,k,nums):
            while j>k:
                if nums[j]>nums[k]:
                    nums[j],nums[k]=nums[k],nums[j]
                    return
                else:
                    j-=1
    def reverser(self,l,r,nums):
            while l<=r:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                r-=1
                
