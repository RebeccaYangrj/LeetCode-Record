# for loop every character, using this char as center to make palindromic 
# longest: maxx
# when using char as center, two types:
# 1. even, char in the left side middle(since we circle from left to right)
# 2. odd, char in the exact middle
# def check palindromic lenth as a function (center l , center r)

# string 
# maxx = max(maxx,odd,even, key = len) 
# according to the len return string result

# time: O(n)
# space: O(1)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxx = ""
        for i in range(len(s)):
            # odd:
            odd = self.palindromic(i-1,i+1,s)
            # even:
            even = self.palindromic(i,i+1,s)
            maxx = max(maxx,odd,even, key = len) 
            # according to the len return string result
        return maxx
        
    def palindromic(self,l,r,s):
        while l>=0 and r<len(s) and s[l]==s[r]:
            l -=1
            r +=1
        # check l and r and one more or not 
        return s[l+1:r]
    
