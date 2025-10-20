class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        size = len(nums)
        i = 0
        result = []
        while i < size:
            correct = nums[i] - 1  #N starts from 1
            if correct < size and nums[correct] != nums[i]:
                nums[i],nums[correct]=nums[correct], nums[i]
            else:
                i += 1
        # return nums
        for i in range(size):
            miss = i+1
            if nums[i] != miss:               
                result.append(miss)
        return result
