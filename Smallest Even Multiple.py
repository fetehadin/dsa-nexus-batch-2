class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        for i in range(1,n+1):
            if i%2 == 0 and i%n == 0:
                return i
        else:
            return 2*n
        
