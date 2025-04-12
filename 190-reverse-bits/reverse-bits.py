class Solution:
    def reverseBits(self, n: int) -> int:
        binary_str = '{:032b}'.format(n)
        
        reversed_binary_str = binary_str[::-1]
        
        result = int(reversed_binary_str, 2)
        
        return result