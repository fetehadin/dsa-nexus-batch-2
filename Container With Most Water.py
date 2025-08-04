class Solution:
    def maxArea(self, height: List[int]) -> int:
        first , last,result = 0, len(height)-1,0
        z = len(height)-1        
        while first < last:
            if height[first]<height[last]:
                if result<height[first]*z:
                    result = height[first]*z               
                first+=1
            else:              
                if result<height[last]*z:
                    result = height[last]*z
                last-=1
            z -= 1
        return result
