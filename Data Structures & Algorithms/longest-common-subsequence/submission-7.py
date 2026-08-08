class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        lcs = [[0] * len(text1) for _ in range(len(text2))]
        n1 = len(text1)
        n2 = len(text2)

        for t1 in range(n1):
            for t2 in range(n2):
                up = lcs[t2][t1-1] if t1-1>=0 else 0
                left = lcs[t2-1][t1] if t2-1>=0 else 0
                diagonal = lcs[t2-1][t1-1] if t2-1>=0 and t1-1>=0 else 0
                lcs[t2][t1] =  diagonal + 1 if text1[t1] == text2[t2] else max(up,left)
        
        return lcs[n2-1][n1-1]

        