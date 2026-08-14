class Solution(object):
    def flipAndInvertImage(self, image):
        a=[]
        for i in image:
            i=i[::-1]
            a.append(i)
        b=[]
        for i in a:
            c=[]
            for j in i:
                if j==0:
                    c.append(1)
                else:
                    c.append(0)
            b.append(c)
        return b
