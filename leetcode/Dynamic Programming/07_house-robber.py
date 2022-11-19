# Dynamic Programming - House Robber - https://leetcode.com/problems/house-robber/discussion/
# M(k) = k번째 집에 있는 돈
# P(0) = M(0)
# P(1) = M(1)
# P(k) = max(P(k-2)+M(k), P(k-1))
class Solution:
    def rob(self, nums: List[int]) -> int:
        res = [0 for i in range(len(nums))]

        for i in range(len(nums)) :
            if i < 1 :
                res[i] = nums[i]
            else :
                res[i] = max(res[i-2]+nums[i],res[i-1])

        return res[-1]
