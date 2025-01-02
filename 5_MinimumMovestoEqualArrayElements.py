class Solution:
  def minMoves2(self, nums: List[int]) -> int:
    # Calculate the median
    nums.sort()
    n = len(nums)
    median = nums[n // 2]
    # Calculate the sum of absolute differences from the median
    moves = 0
    for num in nums:
        moves += abs(num - median)
    
    return moves