class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        for i in ransomNote:
            if ransomNote.count(i)>magazine.count(i):
                return False
        return True
        