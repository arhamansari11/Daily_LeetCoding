class Solution:
    def largestGoodInteger(self, num: str) -> str:
        arr = ["999", "888", "777", "666", "555", "444", "333", "222", "111", "000"]
        
        for i in arr:
            if i in num: 
                return i 
        return "" 