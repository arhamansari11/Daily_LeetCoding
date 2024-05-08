class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        array = []

        array1 = []


        for i in range(len(candies)):
            sum1 = candies[i] + extraCandies
            array.append(sum1)
            
        length = len(array1)

        for j in range(len(array)):
            if array[j]  >= max(candies):
                array1.append(True)
            else:
                array1.append(False)
        
        return array1