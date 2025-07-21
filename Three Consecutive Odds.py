```python3 []
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        consCount = 0
        for num in arr:
            if num %2 != 0:
                consCount +=1
                if consCount == 3:
                  return True        
            else:
                    consCount = 0
        return False

```
