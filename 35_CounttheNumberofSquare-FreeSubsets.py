class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        cnt, mod = Counter(nums), 10**9+7
        for num in (2,3,5,7,11,13):
            cnt[num] += 1
        res = ((cnt[6]*cnt[5] + cnt[2]*cnt[15] + cnt[30]) * cnt[7]\
            + (cnt[2]*cnt[5] + cnt[10]) * (cnt[3]*cnt[7] + cnt[21])\
            + (cnt[3]*cnt[5] + cnt[15]) * cnt[14])\
            * cnt[11] * cnt[13] % mod\
            + (cnt[22]*cnt[13] + cnt[26]*cnt[11])\
            * ((cnt[3]*cnt[5] + cnt[15])*cnt[7] + cnt[21]*cnt[5]) % mod

        for num in (17,19,23,29):
            res = res*(cnt[num]+1)%mod
        return (res*pow(2,cnt[1],mod)-1)%mod