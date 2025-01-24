from typing import List

class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        start_set = set()
        for word in startWords:
            start_set.add(frozenset(word))
        
        count = 0
        for target in targetWords:
            target_set = frozenset(target)
            for char in target:
                if target_set - {char} in start_set:
                    count += 1
                    break
        
        return count

# Example test cases
solution = Solution()
print(solution.wordCount(["ant", "act", "tack"], ["tack", "act", "acti"]))  # Output: 2
print(solution.wordCount(["ab", "a"], ["abc", "abcd"]))  # Output: 1