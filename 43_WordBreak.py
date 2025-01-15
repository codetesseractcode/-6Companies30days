class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #initialize dp array to [False] at the (len(s) + 1)
        dp = [False] * (len(s) + 1)
        #initialize dp[len(s)] = True for tabulation bottom up dynamic programming
        dp[len(s)] = True

        #iterate through the rest of len(s) in reverse for i
        for i in range(len(s) - 1, -1, -1):
            #iterate through word w in wordDict
            for w in wordDict:
                #Check if i + len(w) is less than or equal to len(s) for it to be inbounds and s[i : i + len(w)] == w
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    #Update dp[i] to dp[i + len(w)]
                    dp[i] = dp[i + len(w)]
                #Check if dp[i] is True
                if dp[i]:
                    #break as we don't need to iterate for other words
                    break

        #return the tabulated value in dp[0]
        return dp[0]