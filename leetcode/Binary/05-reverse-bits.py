# binary - reverse-bits - https://leetcode.com/problems/reverse-bits/submissions/
class Solution:
    def reverseBits(self, n: int) -> int:
        reverseBin = bin(n)[2:] # 문자열로 변환하여 풀음
        zero = "0" * (32 - len(reverseBin))
        reverseBin = zero + reverseBin
        
        reverseBin = reverseBin[::-1]
        res = int('0b'+reverseBin, 2)
                
        return res
      
      
      
 # 다른 풀이 - 비트 연산자를 이용하여 풀기
"""
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        
        for i in range(32) :
            res = (res << 1) ^ (n & 1)
            n = n >> 1
        
        return res
"""
