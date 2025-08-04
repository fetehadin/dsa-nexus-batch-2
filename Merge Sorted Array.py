class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        first = 0
        second = 0
        while first < len(nums1) and second < len(nums2):
            if nums1[first]!=0:
                first += 1
            else:
                nums1[first]=nums2[second]
                second += 1
                first += 1
        nums1.sort()
        
