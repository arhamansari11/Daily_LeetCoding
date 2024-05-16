class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen = set()
        double = set()

        for num in nums:
            if num in seen:
                double.add(num)
            else:
                seen.add(num)

        return list(double)