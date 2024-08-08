class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        arr = []
        while len(nums) > 0:
            alice = nums.pop(0)
            bob = nums.pop(0)
            arr.append(bob)
            arr.append(alice)

        return arr
