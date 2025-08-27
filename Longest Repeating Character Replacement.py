class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count , result , l , max_repeat = {},0,0,0
        for r in range(len(s)):
            count[s[r]]=1 + count.get(s[r],0)
            max_repeat = max(max_repeat,count[s[r]])
            while r-l + 1 - max_repeat > k:
                count[s[l]] -= 1
                l += 1
            result = max(result, r-l +1)
        return result
