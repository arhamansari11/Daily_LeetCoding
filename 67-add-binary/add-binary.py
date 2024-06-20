class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a1 =int(a , 2)
        b1 =int(b , 2)  
        add = a1 + b1
        binary = bin(add)[2:]
        return binary