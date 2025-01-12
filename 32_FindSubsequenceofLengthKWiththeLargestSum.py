class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        tuple_heap = [] # Stores (value, index) as min heap
        for i, val in enumerate(nums):
            if len(tuple_heap) == k:
                heappushpop(tuple_heap, (val, i)) # To prevent size of heap growing larger than k
            else:
                heappush(tuple_heap, (val, i))
		# heap now contains only the k largest elements with their indices as well.
        tuple_heap.sort(key=lambda x: x[1]) # To get the original order of values. That is why we sort it by index(x[1]) & not value(x[0])
        ans = []
        for i in tuple_heap:
            ans.append(i[0])
        return ans