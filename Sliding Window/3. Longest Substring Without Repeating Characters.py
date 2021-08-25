# condition : 
#1. substring len (r-l+1)(idx) r move l stay 
#2. longest(maxx) 
#3. not repeat: l,r pointer, dic store the char its idx (for renew l)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        dic = {}
        maxx = 0
        for r in range(len(s)):       
            if s[r] in dic and l <= dic[s[r]]: 
# s[r] in s[l:r] 只有在检查的范围内重复才更新。 比如 "twwabcdeft" 当r到最后一位的时候 他出现过，但是t没出现在我们检查的范围内，所以r-l+1要更新（进入else的循环）而不是不更新了
                l = dic[s[r]]+1
            else:
                maxx = max(maxx,r-l+1)
            dic[s[r]] =r
        return maxx
#time O(n)
#spaceO(n)
