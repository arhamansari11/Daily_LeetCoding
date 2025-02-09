class Solution:
    def smallestNumber(self, nums: int) -> int:
        if nums == 0:
            return 0

        num_str = str(abs(nums))
        digits = sorted(num_str)

        if nums > 0:
            if digits[0] == "0":
                for i in range(1 , len(digits)):
                    if digits[i] != "0":
                        digits[0] , digits[i] = digits[i] , "0"
                        break


            return int("".join(digits))

        else:
            return -int("".join(sorted(num_str , reverse=True)))