# Dynamic Programming - Combination Sum - https://leetcode.com/problems/combination-sum-iv/submissions/844237207/
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        l = [0 for i in range(target+1)]

        for i in range(1,target+1,1) :
            for j in range(len(nums)) :
                if nums[j] == i :
                    l[i] += 1 
                if i-nums[j] >=0 :
                    l[i] += l[i-nums[j]]

        return l[target]
