from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # Sort the input array
        nums.sort()
        n = len(nums)
        # Arrays to store the length of the divisible subset and previous indices
        a = [1] * n
        prev = [-1] * n
        max_len, max_index = 0, -1

        # Dynamic programming to find the length of the largest divisible subset
        for i in range(n):
            for j in range(i - 1, -1, -1):
                if nums[i] % nums[j] == 0 and a[j] + 1 > a[i]:
                    # Update the subset length and previous index
                    a[i] = a[j] + 1
                    prev[i] = j

            # Update the maximum length and its corresponding index
            if a[i] > max_len:
                max_len = a[i]
                max_index = i

        # Reconstruct the largest divisible subset
        result = []
        while max_index != -1:
            result.append(nums[max_index])
            max_index = prev[max_index]

        # Return the result
        return result