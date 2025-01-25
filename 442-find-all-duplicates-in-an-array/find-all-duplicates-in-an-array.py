class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        set1 =  set()
        set2 = set()

        for i in nums:
            if i in set1:
                set2.add(i)
            else:
                set1.add(i)

        return list(set2)