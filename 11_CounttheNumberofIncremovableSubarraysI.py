class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        res, n = 0, len(nums)
        nums.extend([51, 0])
        def is_strictly_increasing(i: int, j: int) -> bool:
            while i < j:
                if nums[i] >= nums[i + 1]: return False
                i += 1
            return True
        
        for i in range(n):
            for j in range(i, n):
                if is_strictly_increasing(0, i - 1) and \
                    is_strictly_increasing(j + 1, n - 1) and \
                    nums[i - 1] < nums[j + 1]: res += 1
        return res