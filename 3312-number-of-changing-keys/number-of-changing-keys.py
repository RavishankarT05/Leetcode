class Solution(object):
    def countKeyChanges(self, s):
        a,b=0,1
        count=0
        while b<len(s):
            if s[a].lower()==s[b].lower():
                pass
            else:
                count+=1
            a+=1
            b+=1
        return count


        