# array - find-minimum-in-rotated-sorted-array - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/submissions/
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) < 1 :
            return 0
        else :
            left = 0
            right = len(nums)-1
            
            while nums[left] > nums[right] : # 1 2 3 4 5 정렬되어 있는 경우
                middle = (left+right)//2
                
                if nums[middle] < nums[right] : # 4 5 1 2 3 / 5 1 2 3 4 - middle 포함 왼쪽에 있는 경우
                    right = middle
                else : # 2 3 4 5 1 / 3 4 5 1 2 - middle 보다 오른쪽에 있는 경우
                    left = middle+1

            return nums[left]
