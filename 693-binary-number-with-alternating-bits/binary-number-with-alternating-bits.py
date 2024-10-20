class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binary = bin(n)
        string = binary[2:]
        boolean = True
        for i in range(len(string) - 1):
            if string[i] == string[i+1]:
                boolean = False
                break

        return boolean

                

        