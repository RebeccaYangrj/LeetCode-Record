class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
# use hashtable to remember , so we can save time for go through everything again:
        dic = {}
        for i,num in enumerate(nums):
            if target - num in dic:
                return [dic[target-num],i]
            dic[num]=i
# 1. brute force: time: O(n2) space: O(n2)  : with one for loop inside another for loop: if nums[i]+nums[j] == target
# 2. two path hashmap: time: O(2n) space: O(n): with 2 for loop: first loop store nums[i], second loop check target - nums[i] in dic or not 
# 3. one path hashmaptime: O(2n) space: O(n)
#time : O(n)
#space: O(n)
