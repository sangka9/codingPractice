# binary - counting-bits - https://leetcode.com/problems/counting-bits/submissions/
class Solution:
    def countBits(self, n: int) -> List[int]:
        cnt = []
        two = [2]
        index = 0
        
        for i in range(1,16) :
            two.append(two[i-1]*2)
        
        for i in range(n+1) :
            if i == 0 :
                cnt.append(0)
            elif i == 1 :
                cnt.append(1)
            elif i > 1 :
                if i in two : # 2의 제곱수 확인
                    index = 1
                    cnt.append(1)
                else :
                    cnt.append(cnt[index] + 1)
                    index += 1
        
        return cnt
    

# 다른 풀이
"""
class Solution:
    def countBits(self, n: int) -> List[int]:
        cnt = [0]
        
        for i in range(1,n+1) :
            cnt.append(cnt[i&(i-1)]+1) # 비트연산자를 이용하여 구하기
        
        return cnt
"""
