class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l , r = 0 , len(numbers)-1

        while l < r :
            current = numbers[l] + numbers[r]
            if current == target:
                return [l+1 , r+1] 
            elif current < target:
                l +=1
            else:
                r -=1
        return []