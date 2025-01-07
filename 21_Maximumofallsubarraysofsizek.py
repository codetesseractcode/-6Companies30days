from collections import deque

class Solution:
    #Function to find maximum of each subarray of size k.
    def maxOfSubarrays(self, arr, k):
        # Initialize deque and result list
        dq = deque()
        result = []
        n = len(arr)
        
        # Process first k elements of array
        for i in range(k):
            # Remove smaller elements as they won't be maximum
            while dq and arr[i] >= arr[dq[-1]]:
                dq.pop()
            dq.append(i)
        
        # Process rest of the elements
        for i in range(k, n):
            # Current window's maximum
            result.append(arr[dq[0]])
            
            # Remove elements outside current window
            while dq and dq[0] <= i - k:
                dq.popleft()
            
            # Remove smaller elements in current window
            while dq and arr[i] >= arr[dq[-1]]:
                dq.pop()
                
            dq.append(i)
        
        # Append maximum element of last window
        result.append(arr[dq[0]])
        
        return result