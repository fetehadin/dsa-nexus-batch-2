class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        win_sum =sum(nums[:k])
        max_sum = win_sum/k
        for num in range(k,len(nums)):
            win_sum += nums[num]
            win_sum -= nums[num-k]
            max_sum = max(max_sum, win_sum/k)
        return max_sum
