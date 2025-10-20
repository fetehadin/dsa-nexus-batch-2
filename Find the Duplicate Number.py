class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        size = len(nums)
        i = 0 
        while i < size:
            correct = nums[i]-1
            if correct < size and nums[i]!= nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1
        # return nums
        for i in range(size):
            # correct = nums[i]-1
            if nums[i] != nums[correct] or nums[i]==nums[i-1]:
                return nums[-1]
