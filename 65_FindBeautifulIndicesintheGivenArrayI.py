class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        sw = {}
        
        for ss in startWords:
            sw[ss] = Counter(ss)
            
        
        S = set()
        
        for target in targetWords:
            counter_t = Counter(target)
            
            for ss in sw:
                if len(target) == len(ss) + 1 and len(counter_t.keys()) == len(sw[ss].keys()) + 1:
                    s = sum([val for key, val in (sw[ss] & counter_t).items()])
                    if s == len(ss):
                        S.add(target)
                        break

        return len(S)