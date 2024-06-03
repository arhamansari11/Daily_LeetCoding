class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        arr = []

        for i in candies:
            add = i + extraCandies
            arr.append(add)

        arr2 = []

        for i in arr:
            if i >= max(candies):
                arr2.append(True)
            else:
                arr2.append(False)

        return arr2