class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        dp = [[-1 for _ in range(n)] for _ in range(m)]

        def solve(i, j):
            if i < 0 or j < 0:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            if text1[i] == text2[j]:
                dp[i][j] = solve(i-1, j-1) + 1
            else:
                dp[i][j] = max(solve(i-1, j), solve(i, j-1))
            
            return dp[i][j]
        
        return solve(m-1, n-1)


"""
dp[i][j] = the longest common subsequence between text1 and text2 at the ith index of text1 and the jth index of text2

dp[0][3] =  c
            crab = 1

for dp[0][3], if text1[0] == text[2], then dp[0][3] = dp[0][2] + 1

for dp[2][3], if text1[2] == text[3], then dp[2][3] = max(dp[1][3], dp[2][2]) + 1
    
"""
        
