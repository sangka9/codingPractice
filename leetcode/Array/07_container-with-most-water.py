# array - container-with-most-water - https://leetcode.com/problems/container-with-most-water/submissions/
# O(n) 으로 찾는 경우
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxWater = 0
        left = 0
        right = len(height)-1
        
        while left < right :
            maxWater = max(maxWater, min(height[left],height[right])*(right-left))
            
            if height[left] < height[right] :
                left += 1
            else :
                right -= 1
        
        
        return maxWater
