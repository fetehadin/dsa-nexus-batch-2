class Solution:
    def countSort(self,s):
        s_new= list(s)
        count = [0]*26
        for char in s:
            index = ord(char)-ord('a')
            count[index]+=1
        target = 0
        for index,value in enumerate(count):
            for i in range(value):
                s_new[target]=chr(index + ord('a'))
                target+=1
        return ''.join(s_new)
        # for i in range(size):
        #     for j in range(size-i-1):
        #         if s_new[j]>s_new[j+1]:
        #             s_new[j],s_new[j+1]=s_new[j+1],s_new[j]
        # return ''.join(s_new)
        # # code here
