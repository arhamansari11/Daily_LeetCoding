class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a = nums[0]
        b = nums[1]
        c = nums[2]
        for i in range(len(nums)-2):
            if a + b > c and b + c > a and a + c > b:
                if nums[i] == nums[i+1] and nums[i+1] == nums[i+2]:
                    return "equilateral"
                elif nums[i] == nums[i+1] or nums[i] == nums[i+2] or nums[i+1] == nums[i+2]:
                    return "isosceles"
                elif nums[i] != nums[i+1] or nums[i] != nums[i+2] or nums[i+1] != nums[i+2]:
                    return "scalene"
            else:
                return "none"

