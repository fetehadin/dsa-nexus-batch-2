class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats , light , heavy = 0,0, len(people) - 1        
        while light <= heavy:
            if people[light]+people[heavy]<=limit:
                light += 1
            boats+=1
            heavy-=1
        return boats
