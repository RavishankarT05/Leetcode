class Solution(object):
    def reverseWords(self, s):
        s=list(s.split())
        z=[]
        for i in s:
            i=list(i)
            a,b=0,len(i)-1
            while a<b:
                i[a],i[b]=i[b],i[a]
                a+=1
                b-=1
            y=''.join(i)
            z.append(y)
        return ' '.join(z)
                