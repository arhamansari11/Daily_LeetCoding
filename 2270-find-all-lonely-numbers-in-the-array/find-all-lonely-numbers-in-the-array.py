class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        num_set = set(nums)
        arr = []
        for i in nums:
            if freq[i] == 1 and (i+1) not in num_set and (i-1) not in num_set:
                arr.append(i)


        return arr