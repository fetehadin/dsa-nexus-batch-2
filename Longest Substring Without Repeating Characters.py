class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l , longest = 0,0
        n = len(s)
        sub_set = set()
        for r in range(n):
            while s[r] in sub_set:
                sub_set.remove(s[l])
                l += 1
            sub_set.add(s[r])
            w = (r-l)+1
            longest = max(longest, w)
        return longest
