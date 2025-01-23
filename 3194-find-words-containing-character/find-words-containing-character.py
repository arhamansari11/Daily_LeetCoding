class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        arr = []
        for i in range(len(words)):
            if words[i].__contains__(x):
                arr.append(i)
        return arr