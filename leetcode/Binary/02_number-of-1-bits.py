# binary - number-of-1-bits - https://leetcode.com/problems/number-of-1-bits/submissions/
class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        
        while n > 0 :
            if n % 2 == 1 :
                cnt += 1
            n /= 2
            n = int(n)
            
        return cnt
