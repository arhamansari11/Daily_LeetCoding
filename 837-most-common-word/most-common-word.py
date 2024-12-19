class Solution:
    def mostCommonWord(self, p: str, banned: List[str]) -> str:
        p = p.lower()
        for i in range(len(banned)):
            p = p.replace(banned[i] , "")
        string = ""
        for i in p:
            if i.isalpha() or i == " ":
                string += i
            else:
                string += " "
        coma = string.split()
        freq = {}
        for i in coma:
            freq[i] = 1 + freq.get(i , 0)

        max_occur = 0
        w = ""
        for i,j in freq.items():
            if j >= max_occur:
                max_occur = j
                w = i 
        return w