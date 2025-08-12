class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result , sp_idx = [],0
        for i,char in enumerate(s):
            if sp_idx < len(spaces) and i == spaces[sp_idx]:
                result.append(' ')
                sp_idx+=1
            result.append(char)
        return ''.join(result)
