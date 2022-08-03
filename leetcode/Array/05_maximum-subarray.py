# array - maximum-subarray - https://leetcode.com/problems/maximum-subarray/submissions/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        start = 0
        end = 1
        maxSum = max(nums)
        tmpSum = sum(nums[start:end])
        
        if len(nums) == 1 :
            return nums[0]
            
        while end < len(nums) :
            if tmpSum > 0 :
                tmpSum += nums[end]
                end += 1
                if tmpSum > maxSum :
                    maxSum = tmpSum
            else :
                start = end
                end += 1
                tmpSum = nums[start]
        
        return maxSum
        
        """ 다른풀이
        for i in range(1,len(nums)) :
            nums[i] = max(nums[i-1]+nums[i],nums[i])
        return max(nums)
        """
