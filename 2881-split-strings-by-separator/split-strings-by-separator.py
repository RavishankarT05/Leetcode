class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        arr=[]
        for i in words:
            a=[]
            for j in i:
                if j==separator:
                    if a:
                        arr.append(''.join(a))
                        a=[]
                else:
                    a.append(j)
            if a:
                arr.append(''.join(a))
        return arr