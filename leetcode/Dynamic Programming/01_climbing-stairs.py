# Dynamic Programming - climbing-stairs - https://leetcode.com/problems/climbing-stairs/submissions/
class Solution:        
    def climbStairs(self, n: int) -> int:
        l = [0,1,2]
        
        for i in range(3,n+1) :
            l.append(l[i-1]+l[i-2])
            
        return l[n]
