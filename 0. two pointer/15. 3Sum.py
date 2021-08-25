# all the nums: backtrack, but nums <= 3000, it will tle

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # such that i != j, i != k, and j != k
        res = []
        
        
        # not contain duplicate: 跳过！
        # for : if ...: continue
        # while:  while xx == x: l+=1
        for i in range(len(nums)-2):
            if nums[i-1]==nums[i] and i>0:
                continue
            # 每次循环都需要冲新r和l开始
            l = i+1
            r = len(nums)-1
            nums[i]
            while l < r:
                if nums[l]+nums[r]+nums[i]>0:
                    r -=1 # sorted可以帮助决定移动哪一位
                elif nums[l]+nums[r]+nums[i]<0:
                    l +=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    l+=1
                    r-=1
                # 双指针一定要最后再加减一位
        return res
                      


                
                    
        
            
            
        
