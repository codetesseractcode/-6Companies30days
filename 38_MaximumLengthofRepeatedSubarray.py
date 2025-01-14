class Solution:                 
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        
        n1, n2 = len(nums1), len(nums2)          
        memo = [[0]*(n2+1) for _ in range(n1+1)]                    # <-- 1)
        
        for idx1 in range(n1)[::-1]:
            for idx2 in range(n2)[::-1]:
                
                if nums1[idx1] == nums2[idx2]:
                    memo[idx1][idx2] = 1 + memo[idx1+1][idx2+1]     # <-- 2)
       
        return max(chain(*memo))                                    # <-- 3)