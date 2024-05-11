class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        seti = set(nums)
        listi = list(seti)
        listi.sort()
        listi.reverse()

        if len(listi) >= 3:
            return listi[2]
        
        return max(nums)
