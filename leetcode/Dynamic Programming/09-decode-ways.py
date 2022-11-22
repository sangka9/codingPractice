# Dynamic Programming - Decode Ways - https://leetcode.com/problems/decode-ways/description/
class Solution:
    def numDecodings(self, s: str) -> int:
        res = [0 for i in range(len(s))]

        for i in range(len(s)) :
            if i == 0 :
                if 0 < int(s[0]) < 10 :
                    res[i] = 1
                else :
                    break
            elif i == 1 :
                if int(s[i-1:i+1]) == 10 or int(s[i-1:i+1]) == 20 :
                    res[i] = 1
                elif int(s[i]) == 0:
                    break
                elif 10 < int(s[i-1:i+1]) < 27  :
                    res[i] = res[i-1] + 1
                else :
                    res[i] = res[i-1]
            else:
                if int(s[i-1:i+1]) == 0 :
                    break
                elif int(s[i-1:i+1]) == 10 or int(s[i-1:i+1]) == 20:
                    res[i] = res[i-2]
                elif int(s[i]) == 0:
                    break
                elif 10 < int(s[i-1:i+1]) < 27  :
                    res[i] = res[i-1] + res[i-2]
                else :
                    res[i] = res[i-1]

        return res[-1]
