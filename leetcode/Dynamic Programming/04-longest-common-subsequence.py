# Dynamic Programming - Longest Common Subsequence - https://leetcode.com/problems/longest-common-subsequence/
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        lcs = [[0]*(len(text2)+1) for i in range(len(text1)+1)] 
        
        for i in range(len(text1)) :
            for j in range(len(text2)) :
                if text1[i] == text2[j]:
                    lcs[i+1][j+1] = lcs[i][j]+1
                else :
                    lcs[i+1][j+1] = max(lcs[i][j+1],lcs[i+1][j])
        
        return lcs[-1][-1]
