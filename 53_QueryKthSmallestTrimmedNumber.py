class Solution:
  def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        def countingSort(indices, pos):
            count = [0] * 10
            for idx in indices:
                count[ord(nums[idx][pos]) - ord('0')] += 1
            start_pos = list(accumulate([0] + count, add))
            result = [None] * len(indices)
            for idx in indices:
                digit = ord(nums[idx][pos]) - ord('0')
                result[start_pos[digit]] = idx
                start_pos[digit] += 1
            return result
            
        n = len(nums)
        m = len(nums[0])
        suffix_ordered = [list(range(n))]
        for i in range(m - 1, -1, -1):
            suffix_ordered.append(countingSort(suffix_ordered[-1], i))
        return [suffix_ordered[t][k-1] for k, t in queries]