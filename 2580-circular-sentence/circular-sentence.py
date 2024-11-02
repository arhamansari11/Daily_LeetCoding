class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words_list = sentence.split()
        count = 0
        for i in range(1 , len(words_list)):
            if words_list[i].startswith(words_list[i-1][-1]):
                count += 1
            
        if words_list[0].startswith(words_list[-1][-1]):
            count += 1

        if count == len(words_list):
            return True
        else:
            return False