class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)
        string = binary[2:]
        arr = list(string)
        for i in range(len(arr)):
            if arr[i] == '0':
                arr[i] = '1'
            elif arr[i] == '1':
                arr[i] = '0'

        string = "".join(arr)
        complement = int(string , 2)

        return complement