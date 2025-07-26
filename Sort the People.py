class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        size = len(heights)
        for i in range(size):
            min_idx=i
            for j in range(i+1,size):
                if heights[min_idx]<=heights[j]:
                    heights[j] , heights[min_idx] = heights[min_idx], heights[j]
                    names[j], names[min_idx] = names[min_idx] , names[j]
        return names
        
                    

        
