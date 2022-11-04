# Dynamic Programming - word-break Problem - https://leetcode.com/problems/word-break/
class Solution:
    def wordBreak(self, s: str, words: List[str]) -> bool:
        tf = [False] * len(s)

        for i in range(len(s)) :
            for j in range(len(words)) :
                if words[j] == s[i-len(words[j])+1:i+1] and (tf[i-len(words[j])] or i-len(words[j]) == -1):
                    tf[i] = True
            print(tf)
        return tf[-1]
