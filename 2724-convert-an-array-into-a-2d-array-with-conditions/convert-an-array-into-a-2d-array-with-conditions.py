class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        arr = []
        while nums:
            two = []
            for num in nums[:]:
                if num not in two:
                    two.append(num)
                    nums.remove(num)
            arr.append(two)

        return arr