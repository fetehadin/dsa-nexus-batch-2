class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        result = []
        size = len(nums)
        i,j = 1,0
        nums.sort()
        # while j<size:
        #     correct = nums[j]-1
        #     if nums[j]!=nums[correct]:
        #         nums[j],nums[correct]=nums[correct],nums[j]
        #     else:
        #         j+=1
        # return nums
        while i < size:
            if nums[i]==nums[i-1]:
                result.append(nums[i])
                break
            else:
                i+=1
        for i in range(size):
            if nums[i]!=i+1 and i+1 not in nums:
                result.append(i+1)
                return result
        return result
