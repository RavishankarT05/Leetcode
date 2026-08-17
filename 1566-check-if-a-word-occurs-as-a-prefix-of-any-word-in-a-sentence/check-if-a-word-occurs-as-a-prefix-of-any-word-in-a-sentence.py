class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        s=sentence.split()
        se=list(searchWord)
        for i in range(len(s)):
            a=list(s[i])
            if len(a)<len(se):
                continue
            z,y=0,0
            while z<len(a) and y<len(se):
                if a[z]==se[y]:
                    z+=1
                    y+=1
                else:
                    break
            if y==len(se):
                return i+1
        return -1
        