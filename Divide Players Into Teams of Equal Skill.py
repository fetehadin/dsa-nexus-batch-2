class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        z = len(skill) 
        skill.sort()    
        first, second , count , output = 0 , z-1  , 0, 0           
        div = sum(skill)/(z/2)               
        if sum(skill)%(z/2)!=0:
            return -1 
        while first < second: 
            if skill[first]+skill[second]==div:
                output += skill[first]*skill[second]
                count += 1                                 
            first += 1              
            second -= 1  
        if count == z/2:
            return output
        else:
            return -1
