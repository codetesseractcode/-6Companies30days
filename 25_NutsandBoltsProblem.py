class Solution:
    def matchPairs(self, n, nuts, bolts):
        # Direct sorting using the character mapping
        char_order = '!#$%&*?@^'
        char_map = {char: idx for idx, char in enumerate(char_order)}
        
        # Sort both arrays based on the character mapping
        temp_nuts = sorted(nuts, key=lambda x: char_map[x])
        temp_bolts = sorted(bolts, key=lambda x: char_map[x])
        
        # Copy sorted elements back to original arrays
        for i in range(n):
            nuts[i] = temp_nuts[i]
            bolts[i] = temp_bolts[i]