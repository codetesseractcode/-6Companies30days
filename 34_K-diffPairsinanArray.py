class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        numSet = set()

        for i in range(n - 1):
            for j in range(i + 1, n):
                if abs(nums[i] - nums[j]) == k:
                    numSet.add((nums[i], nums[j]))
                    numSet.add((nums[j], nums[i]))

        ans = len(numSet)
        if k != 0:
            ans //= 2

        return ans