class Solution(object):
    def uniqueMorseRepresentations(self, words):
        a=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        b=set()
        for i in words:
            c=""
            for j in i:
                c+=a[ord(j)-ord("a")]
            b.add(c)
        return len(b)