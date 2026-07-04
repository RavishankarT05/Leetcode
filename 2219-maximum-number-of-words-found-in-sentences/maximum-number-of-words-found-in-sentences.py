class Solution(object):
    def mostWordsFound(self, sentences):
        max_words=0
        for i in sentences:
            words=len(i.split())
            if words>max_words:
                max_words=words
        return max_words
        