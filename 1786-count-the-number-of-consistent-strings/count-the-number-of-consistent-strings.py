class Solution(object):
    def countConsistentStrings(self, allowed, words):
        count=0
        
        for i in words:
            con=True
            for j in i:
                if j not in allowed:
                    con=False
                    break
                    
            if con:
                print
                count+=1
        return count


                
        