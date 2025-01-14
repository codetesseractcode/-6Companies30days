class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        age = [0] * 121
        total = [0] * 121
        res = 0

        for x in ages:
            age[x] += 1
        
        for x in range(1, 121):
            total[x] = age[x] + total[x-1]
        
        for x in range(15, 121):
            if age[x] == 0: continue

            count = total[x] - total[int(x/2) + 7]
            res += count * age[x] - age[x]
        
        return res