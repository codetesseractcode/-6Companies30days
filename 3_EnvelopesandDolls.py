class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes = sorted(envelopes,key = lambda x: x[1],reverse = True)
        envelopes = sorted(envelopes,key = lambda x: x[0])
        # current = envelopes[0][0]
        dp = [envelopes[0][1]]
        for env in envelopes[1:]:
            if dp[-1] < env[1]:
                dp.append(env[1])
            else:
                i = bisect_left(dp,env[1])
                dp[i] = env[1]
        return len(dp)

        return 0