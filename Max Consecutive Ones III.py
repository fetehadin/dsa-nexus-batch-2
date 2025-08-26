class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeroCount,left,max_count = 0,0,0
        for right in range(len(nums)):
            if nums[right]==0:
                zeroCount += 1
            while zeroCount > k:
                if nums[left]==0:
                    zeroCount -= 1
                left += 1
            max_count = max(max_count, right - left + 1)
        return max_count
