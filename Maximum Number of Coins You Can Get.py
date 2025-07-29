class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        z = len(piles)
        output = 0
        for i in range(int(z/3),z,2):
            output += piles[i]
        return output
