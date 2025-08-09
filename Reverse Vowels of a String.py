class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiou')
        new_s = list(s)
        first , second = 0, len(new_s)-1
        while first < second:
            if new_s[first].lower() in vowels and new_s[second].lower() in vowels:
                new_s[first],new_s[second]=new_s[second],new_s[first]
                first += 1
                second -= 1
            elif new_s[first].lower() in vowels:
                second -= 1
            elif new_s[second].lower() in vowels:
                first += 1
            else:
                first += 1
                second -= 1
        return ("").join(new_s)
