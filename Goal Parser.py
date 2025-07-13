class Solution:
    def interpret(self, command: str) -> str:
        output=''
        i=len(command)
        while i>0:
            for j in range(len(command)):
                if command[j]=='G':
                    output += 'G'
                    i -= 1
                elif command[j]=='(' and command[j+1]==')':
                    output += 'o'
                    i -= 2
                elif command[j]=='(' and command[j+1]=='a':
                    output += 'al'
                    i -= 4
        return output
        
