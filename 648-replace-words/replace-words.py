class Solution:
    def replaceWords(self, words: List[str], string: str) -> str:
        x = string.split()
        for i in range(len(x)):
            for word in words:
                if x[i].startswith(word):
                    x[i] = word
        
        string = " ".join(x)
        return string
