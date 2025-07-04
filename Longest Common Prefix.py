class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ''
        shortest = min(strs,key=len)
        if not strs:
            return common_prefix
        for i in range(len(shortest)):
            current_char = shortest[i]
            for string in strs:
                if string[i]!= current_char:
                    return common_prefix
            common_prefix += current_char
        return common_prefix
            
        
