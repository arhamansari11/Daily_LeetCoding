class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr = []
        for i in nums:
            square = i * i
            arr.append(square)
        

        arr.sort()
        return arr