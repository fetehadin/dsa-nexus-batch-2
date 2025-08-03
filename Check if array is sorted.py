class Solution:
    def isSorted(self, arr) -> bool:
        p1 = 0
        p2 = 1
        while p2<len(arr):
            if arr[p1]>arr[p2]:
                return False
            p2 += 1
            p1 += 1
        return True
        
            
