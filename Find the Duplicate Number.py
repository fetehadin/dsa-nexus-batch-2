class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        size , i = len(nums) , 0
        while i < size:
            correct = nums[i]-1
            if nums[i]!= nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1
        for i in range(size):
            if nums[i] != nums[correct] or nums[i]==nums[i-1]:
                return nums[-1]
