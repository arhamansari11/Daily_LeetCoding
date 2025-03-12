class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        maximum = 0
        pos = 0
        neg = 0

        for i in nums:
            if i < 0:
                neg += 1
            elif i > 0:
                pos += 1


        if pos > neg:
            maximum += pos
        elif neg > pos:
            maximum += neg
        else:
            maximum += pos

        return maximum