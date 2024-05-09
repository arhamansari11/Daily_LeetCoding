from typing import List
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        arr2 = list(range(1, arr[-1] + k + 1))
        temp= []
        for elements in arr2:
            if elements not in arr:
                temp.append(elements)

        return temp[k-1]