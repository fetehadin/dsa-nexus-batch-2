class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        first , second = 0 , len(nums)-1
        count = 0
        nums.sort()        
        while first < second:
            sum = nums[first]+nums[second]
            if sum== k:
                count += 1
                first += 1
                second -= 1
            elif sum>k:
                second -= 1
            else:
                first += 1
        return count
