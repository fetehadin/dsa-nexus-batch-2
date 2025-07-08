class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        rem_num=0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[rem_num] = nums[i]
                rem_num +=1
        return rem_num
