import heapq
class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        # Need to increment minimum number in list at each operation
        prod=1
        min_heap=nums.copy()
        heapq.heapify(min_heap)

        for i in range(k):
            num=min_heap[0]
            heapq.heapreplace(min_heap,num+1)

        for n in min_heap:
            prod=(prod*n)%(10**9+7)

        return prod
