class Solution:
    def stoneGameVI(self, aliceValues, bobValues):
        n = len(aliceValues)
        total_values = [(aliceValues[i] + bobValues[i], i) for i in range(n)]
        total_values.sort(reverse=True)

        alice_score, bob_score = 0, 0
        for idx, (total, i) in enumerate(total_values):
            if idx % 2 == 0:
                alice_score += aliceValues[i]
            else:
                bob_score += bobValues[i]

        if alice_score > bob_score:
            return 1
        elif bob_score > alice_score:
            return -1
        return 0