class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        myList = s.split()
        for i in myList[-1]:
            count += 1
        return count
        
