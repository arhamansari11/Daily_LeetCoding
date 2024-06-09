class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        map = {0: 1}
        prefix_sum = 0
        count = 0
        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k
            if remainder < 0:
                remainder += k
            if remainder in map:
                count += map[remainder]
                map[remainder] += 1
            else:
                map[remainder] = 1
        return count