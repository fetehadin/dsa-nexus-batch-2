class Solution:
    def missingNumber(self, nums: List[int]) -> int: 
        # use cycle sorting method  
        size = len(nums)
        i = 0
        while i < size:
            correct = nums[i]
            if nums[i] < size and nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1
            # return nums
        for i in range(size):
            if nums[i]!= i:
                return i
        return len(nums)
