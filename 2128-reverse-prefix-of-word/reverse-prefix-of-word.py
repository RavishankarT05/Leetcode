class Solution(object):
    def reversePrefix(self, word, ch):
        word=list(word)
        a=[]
        b=word
        for i in b:
            if i==ch:
                a.append(i)
                word=word[1::]
                a=a[::-1]
                return "".join(a)+"".join(word)
            else:
                a.append(i)
                word=word[1::]
        return "".join(b)