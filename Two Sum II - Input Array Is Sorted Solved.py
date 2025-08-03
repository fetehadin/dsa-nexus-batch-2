class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        z = len(numbers)
        first = 0
        second = z-1
        while first < z and second > 0:
            if numbers[first]+numbers[second] == target:
                return [first+1,second+1]
            elif numbers[first]+numbers[second]> target:
                second -= 1
            else:
                first += 1
