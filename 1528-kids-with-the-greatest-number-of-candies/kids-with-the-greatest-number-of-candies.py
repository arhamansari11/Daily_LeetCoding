class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        arr = []
        for i in range(len(candies)):
            extra = candies[i] + extraCandies
            arr.append(extra)
        
        arr2 = []

        for i in range(len(arr)):
            if arr[i] >= max(candies):
                arr2.append(True)
            else:
                arr2.append(False)

        return arr2