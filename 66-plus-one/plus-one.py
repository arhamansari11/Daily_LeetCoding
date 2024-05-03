class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ""
        length = len(digits)
        for i in range(length):
            string = string + str(digits[i])
        num = int(string)
        num = num + 1
        num = str(num)
        ans = []
        for i in range(len(num)):
            ans.append(int(num[i]))
        return ans