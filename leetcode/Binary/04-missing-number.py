# binary - missing-number - https://leetcode.com/problems/missing-number/
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)) :
            if i not in nums :
                res = i
        return res
      
      
#다른 풀이 -> sum 이용
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = (len(nums) * (len(nums)+1)) / 2
        res = int(res)
        
        sumOfNums = sum(nums)
        res = res - sumOfNums
        
        return res
"""
