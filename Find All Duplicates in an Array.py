class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        size , i , result = len(nums) , 0 , []
        if size <= 1:
            return result
        while i < size:
            correct = nums[i]-1
            if nums[i]!= nums[correct]:
                nums[i],nums[correct]=nums[correct],nums[i]
            else:
                i += 1
        for i in range(size):
            if nums[i]!= i+1:
                result.append(nums[i])
        return result
