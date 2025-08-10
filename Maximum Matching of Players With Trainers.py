class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        i , j = 0 , 0
        count = 0
        trainers.sort()
        players.sort()
        while i < len(players) and j < len(trainers):
            if players[i]<=trainers[j]:
                count += 1
                i += 1
                j += 1
            else:
                j += 1
        return count
