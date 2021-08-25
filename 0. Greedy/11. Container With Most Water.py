# MOST Question-Greedy: contains the most water.
# the most: maxx
# containing: lower height* distance = min(height[l],height[r])*(r-l)
# two pointer : two side make a container 
# two pointer need to move so use while l<r (not=since we need distance)
# greedy: every step use the best method
# move the smaller height one, since move the larger height one will cause the volume become small


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        maxx = 0
        while l < r:
            if height[l]<height[r]:
                cur = height[l] *(r-l)
                l += 1
            else:
                cur = height[r] *(r-l)
                r -= 1
            maxx = max(maxx,cur)
        return maxx
    
        
