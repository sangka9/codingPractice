# array - product-of-array-except-self - https://leetcode.com/problems/product-of-array-except-self/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        if nums.count(0) > 1 :
            return [0 for i in range(len(nums))]
        elif nums.count(0) == 1 :
            sum = 1
            for i in range(len(nums)) :
                if nums[i] != 0 :
                    answer.append(0)
                    sum *= nums[i]
            answer.insert(nums.index(0),sum)
        else :
            sum = 1
            for i in range(len(nums)) :
                sum *= nums[i]
            for i in range(len(nums)) :
                answer.append(int(sum/nums[i]))
        
        return answer
