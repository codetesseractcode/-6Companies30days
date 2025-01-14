class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        freq = {i:words.count(i) for i in words}
        freq = dict(sorted(freq.items(),key=lambda k:k[1],reverse=True))

        group = {}

        for val in freq.values():
            if val not in group:
                group[val] = sorted([i for i,j in freq.items() if j == val])
        
        out = [j for i in list(group.values()) for j in i]

        return out[:k]